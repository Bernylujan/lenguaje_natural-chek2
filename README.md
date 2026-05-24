# Procesamiento de Lenguaje Natural: Frankenstein

## 📚 Descripción

Proyecto académico que aplica técnicas de **Procesamiento de Lenguaje Natural (PLN)** al clásico "Frankenstein" de Mary Wollstonecraft Shelley. 

El objetivo es demostrar el pipeline completo de normalización y lematización de texto, desde la ingesta cruda hasta la obtención de tokens normalizados listos para modelado.

## 🎯 Objetivos

1. **Tokenización**: Descomponer el texto en unidades operables (palabras)
2. **Filtrado**: Eliminar stop words y puntuación que añaden ruido
3. **Normalización**: Convertir a minúsculas y estandarizar formato
4. **Lematización**: Reducir palabras a su forma canónica (lema)
5. **Análisis Comparativo**: Comparar Stemming vs Lematización

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
[4] Análisis Stemming vs Lematización
    ↓
Resultados: CSV + TXT
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

### 3. Ejecutar procesamiento

```bash
python frankenstein_nlp.py
```

## 📁 Estructura del Proyecto

```
frankenstein-nlp/
├── frankenstein_nlp.py              # Script principal
├── libro.txt                        # Texto de Frankenstein (Project Gutenberg)
├── requirements.txt                 # Dependencias congeladas
├── tokens_normalizados.txt          # Salida: tokens procesados
├── stemming_vs_lematizacion.csv     # Salida: análisis comparativo
├── cambios_morfologicos.txt         # Salida: transformaciones detectadas
└── README.md                        # Este archivo
```

## 📈 Resultados Esperados

Al ejecutar el script obtendrás:

1. **tokens_normalizados.txt**: Secuencia de todos los tokens lematizados
2. **stemming_vs_lematizacion.csv**: Tabla comparativa de 500 palabras
3. **cambios_morfologicos.txt**: Lista detallada de transformaciones

### Ejemplo de Salida

```
Original       Stemming      Lematización   ¿Coinciden?
creature       creatur       creature       False
created        creat         create         False
electricity    electr        electricity    True
died           died          die            False
```

## 🔧 Tecnologías Utilizadas

- **spaCy 3.7.2**: Tokenización y lematización con modelos neuronales
- **NLTK 3.8.1**: Stemming (Snowball para inglés)
- **pandas 2.1.3**: Análisis y visualización de datos
- **scikit-learn 1.3.2**: Herramientas ML complementarias

## 📖 Conceptos Clave

### Tokenización
Descompone el texto en palabras individuales, manteniendo información gramatical.

### Stop Words
Palabras como "the", "a", "is" que aportan poco valor semántico.

### Lematización vs Stemming
- **Lematización**: Análisis morfológico que preserva validez lingüística
  - "running" → "run"
  - "fui" → "ir" (maneja irregularidades)
  
- **Stemming**: Corte heurístico de sufijos (más agresivo)
  - "running" → "run"
  - Puede producir resultados no válidos

## 📝 Notas

- El archivo de entrada proviene de [Project Gutenberg](https://www.gutenberg.org/)
- Se procesa el texto completo de Frankenstein (~170k tokens)
- El análisis comparativo se limita a 500 palabras por performance
- Toda la codificación es UTF-8 compatible

## 👤 Autor

Bernardo 

## 📄 Licencia

El texto de Frankenstein es dominio público (Project Gutenberg).
El código es educativo y puede ser reutilizado libremente.
