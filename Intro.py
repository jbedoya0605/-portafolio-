from pathlib import Path
import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Portafolio de Proyectos - IA & Data Science", layout="wide"
)

# Ruta base dinámica para evitar errores al cargar imágenes en Streamlit
BASE_DIR = Path(__file__).resolve().parent

st.title("Proyectos y Ejercicios Prácticos")
st.write(
    "Portafolio guiado:"
)

st.divider()

# Lista de proyectos con imágenes conceptuales específicas
proyectos = [
    {
        "titulo": "Preparación de Datos",
        "descripcion": "Herramienta interactiva para la limpieza, transformación y preparación de datasets.",
        "imagen": "prep_datos.png",  # Ilustración: Robot limpiando/estructurando datos
        "url": "https://aplicacionprepdat-jj8mt52qmcfgt736uta4yp.streamlit.app/",
    },
    {
        "titulo": "App Pronóstico",
        "descripcion": "Modelo predictivo para generación de pronósticos basados en datos históricos.",
        "imagen": "pronostico.png",  # Ilustración: Gráficos de proyección y nube
        "url": "https://app-pronostico-hqdqb94czauia5umjjbonk.streamlit.app/",
    },
    {
        "titulo": "KNN Suelos",
        "descripcion": "Clasificación y análisis de tipos de suelo utilizando el algoritmo K-Nearest Neighbors.",
        "imagen": "knn_suelos.png",  # Ilustración: Análisis de terreno con sensores de IA
        "url": "https://knn-suelos-kz3edv5dx7bxajjdshaj7q.streamlit.app/",
    },
    {
        "titulo": "Módulo de Regresión",
        "descripcion": "Aplicación para modelado, ajuste y evaluación de algoritmos de regresión.",
        "imagen": "modulo_regresion.png",  # Ilustración: Ecuaciones y curvas sobre data
        "url": "https://moduloregresi-n-ttzjynfejxbqbtymtsw6xm.streamlit.app/",
    },
    {
        "titulo": "Preparación Data II",
        "descripcion": "Módulo complementario para procesamiento y estructuración avanzada de datos.",
        "imagen": "prep_data_2.png",  # Ilustración: Cinta y embudo clasificando bloques de datos
        "url": "https://preparaci-n-de-datos-fxl8ap7mstyaasjs3agxxf.streamlit.app/",
    },
    {
        "titulo": "Detector de Anomalías",
        "descripcion": "Sistema de detección de patrones atípicos y valores atípicos (outliers) en datos.",
        "imagen": "detector_anomalias.png",  # Ilustración: Radar buscando un punto atípico (alerta)
        "url": "https://detectoranomalias.streamlit.app/",
    },
    {
        "titulo": "Regresión Guiada",
        "descripcion": "Flujo guiado paso a paso para la construcción e interpretación de modelos regresivos.",
        "imagen": "regresion_guiada.png",  # Ilustración: Personaje guiado en un camino de datos
        "url": "https://regresi-n-guiada-yaqfzuwhscmhxfyryfb7ft.streamlit.app/",
    },
    {
        "titulo": "Series de Tiempo",
        "descripcion": "Análisis temporal, tendencias y proyección de datos secuenciales.",
        "imagen": "series_tiempo.png",  # Ilustración: Reloj digital con gráficos de línea y tiempo
        "url": "https://series-tiempo-gdqyc7higchmeeaz4mgx7n.streamlit.app/",
    },
]

# Renderizar en cuadrícula de 3 columnas
cols_per_row = 3
for i in range(0, len(proyectos), cols_per_row):
    cols = st.columns(cols_per_row)
    chunk = proyectos[i : i + cols_per_row]

    for idx, proj in enumerate(chunk):
        with cols[idx]:
            st.subheader(proj["titulo"])

            # Cargar imagen y verificar su existencia
            img_path = BASE_DIR / proj["imagen"]
            if img_path.exists():
                st.image(str(img_path), use_container_width=True)

            st.write(proj["descripcion"])
            st.link_button(
                "Abrir aplicación 🚀", proj["url"], use_container_width=True
            )

    st.divider()
