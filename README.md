# Procesamiento de Lenguaje Natural: Frankenstein

## 📚 Descripción

Proyecto académico que aplica técnicas de **Procesamiento de Lenguaje Natural (PLN)** al clásico "Frankenstein" de Mary Wollstonecraft Shelley. 

El proyecto consta de **3 partes**:

1. **Checkpoint 2**: Normalización y Lematización
2. **Checkpoint 3**: Vectorización y Representación Semántica (ACTUAL)

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
