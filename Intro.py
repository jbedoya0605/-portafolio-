from pathlib import Path
import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Portafolio de Proyectos - Data Science & IA",
    page_icon="📊",
    layout="wide",
)

# Título y descripción principal
st.title("Proyectos y Ejercicios Prácticos")
st.write(
    "A continuación encontrarás las aplicaciones de Machine Learning, Ciencia de Datos e Inteligencia Artificial desarrolladas en Streamlit:"
)

st.divider()

# Lista completa de proyectos con URLs directas de imágenes
proyectos = [
    {
        "titulo": "Preparación de Datos",
        "descripcion": "Herramienta interactiva para la limpieza, transformación y preparación de datasets.",
        "imagen": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&q=80",
        "url": "https://aplicacionprepdat-jj8mt52qmcfgt736uta4yp.streamlit.app/",
    },
    {
        "titulo": "App Pronóstico",
        "descripcion": "Modelo predictivo para generación de pronósticos basados en datos históricos.",
        "imagen": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500&q=80",
        "url": "https://app-pronostico-hqdqb94czauia5umjjbonk.streamlit.app/",
    },
    {
        "titulo": "KNN Suelos",
        "descripcion": "Clasificación y análisis de tipos de suelo utilizando el algoritmo K-Nearest Neighbors.",
        "imagen": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500&q=80",
        "url": "https://knn-suelos-kz3edv5dx7bxajjdshaj7q.streamlit.app/",
    },
    {
        "titulo": "Módulo de Regresión",
        "descripcion": "Aplicación para modelado, ajuste y evaluación de algoritmos de regresión.",
        "imagen": "https://images.unsplash.com/photo-1543286386-713bdd548da4?w=500&q=80",
        "url": "https://moduloregresi-n-ttzjynfejxbqbtymtsw6xm.streamlit.app/",
    },
    {
        "titulo": "Preparación Data II",
        "descripcion": "Módulo complementario para procesamiento y estructuración avanzada de datos.",
        "imagen": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=500&q=80",
        "url": "https://preparaci-n-de-datos-fxl8ap7mstyaasjs3agxxf.streamlit.app/",
    },
    {
        "titulo": "Detector de Anomalías",
        "descripcion": "Sistema de detección de patrones atípicos y valores atípicos (outliers) en datos.",
        "imagen": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=500&q=80",
        "url": "https://detectoranomalias.streamlit.app/",
    },
    {
        "titulo": "Regresión Guiada",
        "descripcion": "Flujo guiado paso a paso para la construcción e interpretación de modelos regresivos.",
        "imagen": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=500&q=80",
        "url": "https://regresi-n-guiada-yaqfzuwhscmhxfyryfb7ft.streamlit.app/",
    },
    {
        "titulo": "Series de Tiempo",
        "descripcion": "Análisis temporal, tendencias y proyección de datos secuenciales.",
        "imagen": "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=500&q=80",
        "url": "https://series-tiempo-gdqyc7higchmeeaz4mgx7n.streamlit.app/",
    },
]

# Renderizado en cuadrícula de 3 columnas
cols_per_row = 3
for i in range(0, len(proyectos), cols_per_row):
    cols = st.columns(cols_per_row)
    chunk = proyectos[i : i + cols_per_row]

    for idx, proj in enumerate(chunk):
        with cols[idx]:
            st.subheader(proj["titulo"])
            st.image(proj["imagen"], use_container_width=True)
            st.write(proj["descripcion"])
            st.link_button(
                "Abrir aplicación 🚀", proj["url"], use_container_width=True
            )

    st.divider()
