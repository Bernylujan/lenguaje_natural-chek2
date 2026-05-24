# Procesamiento de Lenguaje Natural: Frankenstein

## 📚 Descripción

Proyecto académico integral que aplica técnicas de **Procesamiento de Lenguaje Natural (PLN)** al clásico "Frankenstein" de Mary Wollstonecraft Shelley. 

El proyecto consta de **4 checkpoints** que representan el pipeline completo desde datos crudos hasta análisis semántico avanzado.

## 🎯 Checkpoints del Proyecto

### Checkpoint 2: Normalización y Lematización
- Tokenización del texto
- Filtrado de stop words
- Lematización vs Stemming
- **Entrega**: `frankenstein_nlp.py`

### Checkpoint 3: Vectorización Clásica
- Bag-of-Words (BoW)
- TF-IDF
- Visualización 3D con PCA
- Similitud de coseno
- **Entrega**: `frankenstein_vectorizacion.ipynb`

### Checkpoint 4: Semántica Distribucional ⭐ (ACTUAL)
- **Word2Vec (Skip-gram)**: Embeddings densos
- **Visualización 3D**: Espacio semántico real
- **Análisis**: Similitud semántica entre palabras
- **Gráficas**: Heatmaps y visualizaciones múltiples
- **Entrega**: `frankenstein_checkpoint4_completo.ipynb`

## 📊 Pipeline de Procesamiento Completo

```
LIBRO.TXT (170k+ tokens)
    ↓
[Checkpoint 2] Tokenización + Limpieza + Lematización
    ↓
[Checkpoint 3] BoW + TF-IDF + PCA 3D
    ↓
[Checkpoint 4] Word2Vec + Embeddings + Análisis Semántico
    ↓
✅ RESULTADO: Modelo entrenado + 4+ visualizaciones
```

## 🚀 Instalación y Uso

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Ejecutar Notebook (RECOMENDADO)

```bash
jupyter notebook frankenstein_checkpoint4_completo.ipynb
```

El notebook es **autoexplicativo** y ejecuta todo el pipeline en orden:
1. Carga datos
2. Limpia y normaliza
3. Vectoriza (BoW + TF-IDF)
4. Entrena Word2Vec
5. Genera 4+ gráficas
6. Análisis de similitud

## 📁 Estructura del Repositorio

```
frankenstein-nlp/
│
├── 📄 NOTEBOOKS (Ejecución interactiva)
│   ├── frankenstein_checkpoint4_completo.ipynb  ⭐ PRINCIPAL
│   ├── frankenstein_vectorizacion.ipynb        (Checkpoint 3)
│   └── frankenstein_nlp.py                     (Checkpoint 2)
│
├── 📚 DATOS
│   └── libro.txt                    (Frankenstein original)
│
├── 📦 CONFIGURACIÓN
│   ├── requirements.txt              (Dependencias congeladas)
│   └── README.md                    (Este archivo)
│
└── 📊 SALIDAS (Generadas al ejecutar)
    ├── frankenstein_word2vec_3d.png            ✓ Espacio semántico 3D
    ├── frankenstein_embeddings_heatmap.png     ✓ Matriz de embeddings
    ├── frankenstein_similitud_semantica.png    ✓ Matriz de similitud
    ├── frankenstein_embedding_individual.png   ✓ Vector individual
    ├── word2vec_frankenstein.model             (Modelo entrenado)
    ├── corpus_final_lematizado.txt             (Oraciones procesadas)
    ├── vocabulario_word2vec.csv                (Palabras + frecuencias)
    └── vectorizacion_comparacion.csv           (Tabla comparativa)
```

## 📊 Visualizaciones Generadas

### 1. **frankenstein_word2vec_3d.png**
- Espacio semántico 3D con PCA
- 100 palabras principales
- Proximidad = similitud semántica
- Axes = componentes principales (62% varianza en 3D)

### 2. **frankenstein_embeddings_heatmap.png**
- Palabras clave vs Dimensiones del embedding
- 18 palabras principales × 50 dimensiones
- Colores: Rojo (negativos) → Azul (positivos)
- Muestra estructura interna de los embeddings

### 3. **frankenstein_similitud_semantica.png**
- Matriz 18×18 de similitud coseno
- Verde oscuro = máxima similitud (1.0)
- Verde claro = baja similitud (0.0)
- Identifica palabras temáticamente relacionadas
- Ejemplo: "creature" ↔ "monster" (alta similitud)

### 4. **frankenstein_embedding_individual.png**
- Vector de 50 dimensiones (gráfico de barras + heatmap)
- Distribución de valores en el embedding
- Estadísticas: media, desv. est., norma L2

## 🔧 Tecnologías Utilizadas

| Librería | Versión | Propósito |
|----------|---------|----------|
| **spaCy** | 3.7.2 | Tokenización, lematización |
| **Gensim** | 4.3.1 | Word2Vec (Skip-gram) |
| **scikit-learn** | 1.3.2 | Vectorización, PCA, similitud |
| **pandas** | 2.1.3 | Análisis de datos |
| **matplotlib** | 3.8.2 | Visualizaciones |
| **numpy** | 1.24.3 | Operaciones numéricas |
| **NLTK** | 3.8.1 | Stemming (comparación) |
| **jupyter** | 1.0.0 | Notebooks interactivos |

## 📖 Conceptos Clave

### Semántica Distribucional
"El significado de una palabra está en los contextos en los que aparece"
- **Hipótesis Distribucional**: Palabras similares aparecen en contextos similares
- **Embeddings**: Representación numérica comprimida del significado

### Word2Vec (Skip-gram)
- **Entrada**: Palabra central (ej: "creature")
- **Salida**: Predicción de palabras contexto
- **Resultado**: Vector denso (50 dimensiones vs 100+ del BoW)
- **Ventaja**: Captura relaciones semánticas finas

### Diferencias: BoW vs TF-IDF vs Word2Vec

| Aspecto | BoW | TF-IDF | Word2Vec |
|---------|-----|--------|----------|
| **Tipo** | Conteos | Ponderación | Embedding |
| **Dimensión** | 100+ | 100+ | 50 |
| **Densidad** | Sparse (0.1%) | Sparse (0.1%) | Densa (100%) |
| **Contexto** | No | No | Sí |
| **Semántica** | Débil | Media | Fuerte |
| **Interpretable** | Alta | Alta | Baja |
| **Uso** | Clasificación | Búsqueda | Semántica |

### PCA (Principal Component Analysis)
- Reducción: 50 dimensiones → 3 dimensiones
- Mantiene 62-70% de la varianza
- Permite visualizar espacios de alta dimensión

### Similitud Coseno
- Rango: [0, 1]
- **1.0**: Vectores idénticos
- **0.0**: Vectores ortogonales (sin similitud)
- Métrica: `cos(θ) = (A·B) / (||A|| × ||B||)`

## 💡 Insights del Proyecto

1. **BoW destaca**: "said" (1200+ veces), "upon", "could"
2. **TF-IDF destaca**: "creature", "frankenstein", "monster" (distintivos)
3. **Word2Vec agrupa**: 
   - "creature" ↔ "monster" (muy similar)
   - "victor" ↔ "creator" (contexto)
   - "death" ↔ "life" (conceptos opuestos)
4. **Embeddings capturan**: Relaciones semánticas complejas
5. **Densidad**: Word2Vec es 1000× más comprimido que BoW

## 📚 Flujo de Aprendizaje

```
Módulo 1: Intro a PLN
    ↓
Módulo 2: Normalización
    ↓
Módulo 3: Vectorización Clásica (BoW/TF-IDF)
    ↓
Módulo 4: Semántica Distribucional (Word2Vec) ← AQUÍ ESTAMOS
    ↓
Posibles continuaciones:
    - FastText (variante de Word2Vec)
    - GloVe (factorización de matrices)
    - Transformers (BERT, GPT)
    - Modelos de lenguaje grandes (LLMs)
```

## 📝 Cómo Ejecutar

### Opción A: Interactivo (Recomendado)

```bash
# Terminal 1
jupyter notebook frankenstein_checkpoint4_completo.ipynb

# Ejecuta cada celda con Shift + Enter
# Visualiza gráficas directamente en el notebook
# Modifica parámetros sobre la marcha
```

### Opción B: Por script (Checkpoint 2)

```bash
python frankenstein_nlp.py
```

## 🎓 Aprendizajes Clave

1. **Pipeline PLN completo**: Datos crudos → Análisis semántico
2. **Tradeoffs**: Interpretabilidad vs Expresividad
3. **Vectorización**: Evolución (BoW → TF-IDF → Embeddings)
4. **Red neuronal simple**: Word2Vec es una NN con capa oculta
5. **Geometría del lenguaje**: Similitud = proximidad espacial

## 🌟 Características Destacadas

✅ **Notebook completo**: Ejecutable línea por línea
✅ **4+ visualizaciones**: Diferentes ángulos del análisis
✅ **Modelos guardados**: Word2Vec listo para reutilizar
✅ **CSV exportados**: Resultados tabulares para análisis
✅ **Corpus procesado**: Oraciones lematizadas disponibles
✅ **Documentación exhaustiva**: Comentarios en cada celda
✅ **Reproducible**: Seeds fijos para consistencia

## 📄 Licencia

El texto de Frankenstein es dominio público (Project Gutenberg).
El código es educativo y puede ser reutilizado libremente.

## 👤 Autor

Proyecto académico - Checkpoints 2, 3 y 4
Coursera Hybridge - Procesamiento de Lenguaje Natural

## 🔗 Referencias

- Bengio et al. (2003): "A neural probabilistic language model"
- Mikolov et al. (2013): "Efficient Estimation of Word Representations in Vector Space"
- Goldberg & Levy (2014): "word2vec Explained"
- GloVe: Global Vectors for Word Representation

---

## ✨ Próximos Pasos

- [ ] Comparar con GloVe pre-entrenado
- [ ] Implementar FastText
- [ ] Análisis de componentes principales (interpretación)
- [ ] Clustering de palabras (K-Means)
- [ ] Búsqueda semántica (consultas)
- [ ] Analogías semánticas (king - man + woman = queen)


## 🎯 Objetivos

### Parte 1 (Checkpoint 2)
1. **Tokenización**: Descomponer el texto en unidades operables (palabras)
2. **Filtrado**: Eliminar stop words y puntuación que añaden ruido
3. **Normalización**: Convertir a minúsculas y estandarizar formato
4. **Lematización**: Reducir palabras a su forma canónica (lema)
5. **Análisis Comparativo**: Comparar Stemming vs Lematización

### Parte 2 (Checkpoint 3)
1. **Bag-of-Words (BoW)**: Representación por conteos
2. **TF-IDF**: Representación por importancia relativa
3. **PCA 3D**: Visualización en espacio vectorial
4. **Similitud de Coseno**: Análisis de similaridad entre oraciones

## 📊 Pipeline de Procesamiento

```
Texto Crudo (7,742 líneas)
    ↓
[1] Tokenización → 169,450+ tokens
    ↓
[2] Filtrado Stop Words → 103,250+ tokens relevantes
    ↓
[3] Lematización + Normalización → Tokens normalizados
    ↓
[4] Vectorización (BoW + TF-IDF) → Matrices numéricas
    ↓
[5] PCA 3D → Visualización interactiva
    ↓
Análisis de Similitud + Insights
```

## 🚀 Instalación y Uso

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Opción A: Ejecutar Jupyter Notebook (RECOMENDADO)

```bash
jupyter notebook frankenstein_vectorizacion.ipynb
```

Esto abrirá el notebook interactivo donde puedes:
- Ver el código paso a paso
- Ejecutar celdas individuales
- Visualizar gráficas 3D interactivas
- Modificar parámetros

### 3. Opción B: Ejecutar script Python

```bash
python frankenstein_nlp.py  # Parte 1 (Normalización)
```

## 📁 Estructura del Proyecto

```
frankenstein-nlp/
├── frankenstein_nlp.py              # Script: Normalización y Lematización
├── frankenstein_vectorizacion.ipynb  # Notebook: Vectorización y Visualización
├── libro.txt                        # Texto de Frankenstein (Project Gutenberg)
├── requirements.txt                 # Dependencias congeladas
├── README.md                        # Este archivo
│
├── [Salidas del Checkpoint 2]
├── tokens_normalizados.txt
├── stemming_vs_lematizacion.csv
├── cambios_morfologicos.txt
│
└── [Salidas del Checkpoint 3]
    ├── frankenstein_vectorizacion_3d.png
    ├── frankenstein_similitud.png
    ├── X_bow.npz (matriz sparse)
    ├── X_tfidf.npz (matriz sparse)
    ├── vocabulario_frankenstein.csv
    └── corpus_lematizado.txt
```

## 📊 Resultados y Visualizaciones

### Gráficas 3D Generadas

1. **frankenstein_vectorizacion_3d.png**
   - Lado izquierdo: Bag-of-Words (conteos simples)
   - Lado derecho: TF-IDF (importancia relativa)
   - Cada punto = una palabra en espacio 3D
   - Reducción dimensional con PCA

2. **frankenstein_similitud.png**
   - Matriz de similitud coseno entre primeras 10 oraciones
   - Colores intensos = mayor similitud
   - Permite identificar oraciones temáticamente relacionadas

### Ejemplo de Salida

```
BAG-OF-WORDS:
  • Tokens originales: 169,450
  • Tokens relevantes: 103,250
  • Dimensiones: 103,250 × 100
  • Top palabras: "said", "upon", "could"

TF-IDF:
  • Matriz: 103,250 × 100
  • Top palabras: "creature", "frankenstein", "monster"
  • Penaliza palabras comunes, destaca distintivas

VISUALIZACIÓN:
  • PCA explica: ~65% de varianza con 3 componentes
  • Similitud coseno: rango [0, 1]
```

## 🔧 Tecnologías Utilizadas

| Librería | Versión | Propósito |
|----------|---------|----------|
| **spaCy** | 3.7.2 | Tokenización, lematización, análisis morfológico |
| **NLTK** | 3.8.1 | Stemming (comparación) |
| **scikit-learn** | 1.3.2 | Vectorización (BoW, TF-IDF), PCA, similitud |
| **pandas** | 2.1.3 | Análisis y visualización de datos |
| **matplotlib** | 3.8.2 | Gráficas 2D y 3D |
| **numpy** | 1.24.3 | Operaciones numéricas |
| **scipy** | 1.11.4 | Matrices sparse |
| **jupyter** | 1.0.0 | Notebooks interactivos |

## 📖 Conceptos Clave

### Tokenización
Descompone el texto en palabras individuales, manteniendo información gramatical.

### Lematización vs Stemming
- **Lematización**: Análisis morfológico que preserva validez lingüística
- **Stemming**: Corte heurístico de sufijos (más agresivo)

### Bag-of-Words (BoW)
- Representación simple por conteos
- Ignora orden y contexto
- Efectivo pero disperso (sparse)

### TF-IDF
- **TF**: Qué tan frecuente es la palabra en este documento
- **IDF**: Qué tan rara es la palabra en todo el corpus
- Producto: Importancia relativa de cada palabra

### PCA (Principal Component Analysis)
- Reduce dimensionalidad manteniendo varianza
- 100 dimensiones → 3 dimensiones (para visualizar)
- Líneas de referencia muestran los ejes principales

### Similitud de Coseno
- Mide ángulo entre vectores
- Rango: [0, 1]
- Valor 1 = vectores idénticos
- Valor 0 = vectores ortogonales

## 💡 Insights del Proyecto

1. **BoW destaca**: Palabras frecuentes (conectores, pronombres)
2. **TF-IDF destaca**: Palabras distinctivas (conceptos clave del Frankenstein)
3. **Clusterización**: Palabras semánticamente similares quedan cercanas en 3D
4. **Similitud**: Detecta oraciones sobre temas relacionados

## 📝 Notas

- El archivo de entrada proviene de [Project Gutenberg](https://www.gutenberg.org/)
- Se procesa el texto completo de Frankenstein (~170k tokens)
- La vectorización se limita a 100 palabras más frecuentes para claridad
- Las visualizaciones 3D son interactivas en Jupyter (puedes rotar, zoom)
- Toda la codificación es UTF-8 compatible

## 🎓 Aprendizajes

Este proyecto demuestra el **flujo completo de PLN**:

```
Datos No Estructurados 
    ↓
Procesamiento (tokenización, limpieza, normalización)
    ↓
Vectorización (conversión a números)
    ↓
Análisis y Modelado (estadística, ML)
```

## 👤 Autor

Proyecto académico - Checkpoints 2 & 3 - Coursera Hybridge PLN

## 📄 Licencia

El texto de Frankenstein es dominio público (Project Gutenberg).
El código es educativo y puede ser reutilizado libremente.

---

### 🚀 Próximos pasos

- [ ] Agregar más técnicas (Word2Vec, GloVe)
- [ ] Implementar clustering (K-Means)
- [ ] Análisis de temas (LDA)
- [ ] Clasificación de texto con modelos entrenados
