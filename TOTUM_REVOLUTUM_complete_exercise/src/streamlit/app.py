import streamlit as st
from PIL import Image
import os, sys
import pandas as pd
import json
import pymysql
from sqlalchemy import create_engine


# Haz que se pueda importar correctamente estas funciones que están en la carpeta utils/
dir = os.path.dirname
sep = os.sep
src_path = dir(dir(os.path.abspath(__file__)))
sys.path.append(src_path)

from utils.stream_config import draw_map
from utils.dataframes import load_csv_for_map

totum_revol_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(totum_revol_path)





menu = st.sidebar.selectbox('Menu:',
            options=["No selected", "Load Image", "Map", "API", "Australia Fire", "Machine Learning"])

if menu == "No selected":
    # Pon el título del proyecto que está en el archivo "config.json" en /config

    config_json_path = totum_revol_path + sep + 'config' + sep + 'config.json'

    with open(config_json_path, "r") as config_json_readed:
        json_config = json.load(config_json_readed)

    st.title(json_config['Title'])
    st.write(json_config['Description'])
    
if menu == "Load Image":

    # Carga la imagen que está en data/img/happy.jpg
    path_image_happy = totum_revol_path + sep + 'data' + sep + 'img' + sep + 'happy.jpg'
    image = Image.open(path_image_happy)
    st.image (image,use_column_width=True)

if menu == "Map":
    # El archivo que está en data/ con nombre 'red_recarga_acceso_publico_2021.csv'
    csv_map_path = totum_revol_path + sep + 'data' + sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)

if menu == "API":
    # Accede al único endpoint de tu API flask y lo muestra por pantalla como tabla/dataframe
    st.title('Play Store')
    dataframe_playstore = pd.read_json('http://localhost:6060/playstore')
    st.table(dataframe_playstore)
    st.balloons()


if menu == "Australia Fire":
    """6"""
    st.title("Fire Table")
    

    # 1. Conecta a la BBDD
    # 2. Obtén, a partir de sentencias SQL (no pandas), la información de las tablas que empiezan por 'fire_archive*' (join)
    # 3. Entrena tres modelos de ML diferentes siendo el target la columna 'fire_type'. Utiliza un pipeline que preprocese los datos con PCA. Usa Gridsearch.  
    # 4. Añade una entrada en la tabla 'student_findings' por cada uno de los tres modelos. 'student_id' es EL-ID-DE-TU-GRUPO.
    # 5. Obtén la información de la tabla 'fire_nrt_M6_96619' y utiliza el mejor modelo para predecir la columna target de esos datos. 
    # 6. Usando SQL (no pandas) añade una columna nueva en la tabla 'fire_nrt_M6_96619' con el nombre 'fire_type_EL-ID-DE-TU-GRUPO'
    # 7. Muestra por pantalla en Streamlit la tabla completa (X e y)
    


