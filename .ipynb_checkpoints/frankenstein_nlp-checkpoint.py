"""
Procesamiento de Lenguaje Natural: Frankenstein
Normalización y Lematización del texto clásico de Mary Shelley

Objetivo: Aplicar técnicas de PLN para limpiar y normalizar el texto
"""

import spacy
import pandas as pd
from nltk.stem import SnowballStemmer
import warnings

warnings.filterwarnings('ignore')

print("=" * 80)
print("PROCESAMIENTO DE LENGUAJE NATURAL: FRANKENSTEIN")
print("=" * 80)

# ============================================================================
# 0. CARGA DE MODELOS
# ============================================================================

print("\n[0] Cargando modelos de spaCy...")
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Descargando modelo en_core_web_sm...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

print("✓ Modelo en_core_web_sm cargado")

# Configurar stemmer para inglés
stemmer = SnowballStemmer("english")

# ============================================================================
# 1. CARGA DE TEXTO
# ============================================================================

print("\n[1] Cargando archivo de texto...")
with open("libro.txt", "r", encoding="utf-8") as f:
    texto_frankenstein = f.read()

print(f"✓ Texto cargado con éxito")
print(f"  - Longitud total: {len(texto_frankenstein):,} caracteres")
print(f"  - Primeras 100 caracteres: {texto_frankenstein[:100]}...")

# ============================================================================
# 2. TOKENIZACIÓN
# ============================================================================

print("\n[2] Tokenización...")
doc = nlp(texto_frankenstein)

print(f"✓ Tokenización completada")
print(f"  - Total de tokens: {len(doc):,}")
print(f"  - Primeros 20 tokens: {[token.text for token in doc][:20]}")

# ============================================================================
# 3. FILTRADO DE STOP WORDS (Eliminación de Ruido)
# ============================================================================

print("\n[3] Filtrado de Stop Words...")

tokens_relevantes = []
tokens_ruido = []

for token in doc:
    if not token.is_stop and not token.is_punct and token.text.strip():
        tokens_relevantes.append(token.text)
    elif token.is_stop:
        tokens_ruido.append(token.text)

print(f"✓ Filtrado completado")
print(f"  - Palabras de ruido eliminadas: {len(tokens_ruido):,}")
print(f"  - Palabras relevantes conservadas: {len(tokens_relevantes):,}")
print(f"  - Reducción: {len(doc):,} → {len(tokens_relevantes):,} tokens")
print(f"  - Ejemplos de stop words: {tokens_ruido[:15]}")

# ============================================================================
# 4. LEMATIZACIÓN Y NORMALIZACIÓN
# ============================================================================

print("\n[4] Lematización y Normalización...")

tokens_normalizados = []
cambios_interesantes = []

for token in doc:
    if not token.is_stop and not token.is_punct and token.text.strip():
        lema = token.lemma_.lower()
        tokens_normalizados.append(lema)
        
        # Capturar cambios significativos
        if token.text.lower() != lema:
            cambios_interesantes.append((token.text.lower(), lema))

print(f"✓ Lematización completada")
print(f"  - Total de tokens normalizados: {len(tokens_normalizados):,}")
print(f"  - Cambios morfológicos detectados: {len(cambios_interesantes):,}")
print(f"\n  Ejemplos de transformaciones (Palabra → Lema):")
for orig, lemma in cambios_interesantes[:15]:
    print(f"    • {orig:15} → {lemma}")

# ============================================================================
# 5. ANÁLISIS COMPARATIVO: STEMMING vs LEMATIZACIÓN
# ============================================================================

print("\n[5] Análisis Comparativo: Stemming vs Lematización...")

data_comparativa = []
count = 0

for token in doc:
    if not token.is_punct and not token.is_space and count < 500:  # Limitamos a 500 para visualización
        raiz_stem = stemmer.stem(token.text)
        lema = token.lemma_
        
        data_comparativa.append({
            "Original": token.text,
            "Stemming": raiz_stem,
            "Lematización": lema,
            "¿Coinciden?": raiz_stem.lower() == lema.lower()
        })
        count += 1

df = pd.DataFrame(data_comparativa)

print(f"✓ Análisis completado")
print(f"\n  Palabras interesantes donde Stemming ≠ Lematización:")

# Palabras clave del Frankenstein donde probablemente haya diferencias
palabras_interesantes = ["creature", "created", "monster", "electricity", "died", "creating", 
                         "love", "loved", "fear", "feared", "tragic", "tragedies"]

for palabra in palabras_interesantes:
    filtro = df[df["Original"].str.lower() == palabra.lower()]
    if not filtro.empty:
        print(f"\n  {filtro.to_string(index=False)}")

print(f"\n  Primeros 15 tokens procesados:")
print(df.head(15).to_string(index=False))

# ============================================================================
# 6. ESTADÍSTICAS FINALES
# ============================================================================

print("\n" + "=" * 80)
print("ESTADÍSTICAS FINALES")
print("=" * 80)

print(f"""
Resumen del Procesamiento:
├─ Tokens originales:        {len(doc):,}
├─ Stop words eliminados:    {len(tokens_ruido):,}
├─ Tokens relevantes:        {len(tokens_relevantes):,}
├─ Tokens normalizados:      {len(tokens_normalizados):,}
├─ Reducción total:          {((1 - len(tokens_normalizados)/len(doc)) * 100):.1f}%
├─ Cambios morfológicos:     {len(cambios_interesantes):,}
└─ Palabras únicas (lemas):  {len(set(tokens_normalizados)):,}

Análisis Stemming vs Lematización:
├─ Registros analizados:     {len(df)}
├─ Coincidencias:            {df['¿Coinciden?'].sum()}
└─ Diferencias:              {(~df['¿Coinciden?']).sum()}
""")

# ============================================================================
# 7. GUARDAR RESULTADOS
# ============================================================================

print("\n[6] Guardando resultados...")

# Guardar tokens normalizados
with open("tokens_normalizados.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(tokens_normalizados))
print("✓ tokens_normalizados.txt guardado")

# Guardar análisis comparativo
df.to_csv("stemming_vs_lematizacion.csv", index=False)
print("✓ stemming_vs_lematizacion.csv guardado")

# Guardar cambios morfológicos
with open("cambios_morfologicos.txt", "w", encoding="utf-8") as f:
    f.write("Cambios Morfológicos Detectados\n")
    f.write("=" * 50 + "\n\n")
    for orig, lemma in cambios_interesantes:
        f.write(f"{orig:20} → {lemma}\n")
print("✓ cambios_morfologicos.txt guardado")

print("\n" + "=" * 80)
print("¡PROCESAMIENTO COMPLETADO!")
print("=" * 80)
