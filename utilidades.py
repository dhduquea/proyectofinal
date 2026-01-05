import streamlit as st
from PIL import Image

def generarMenu():
    with st.sidebar:
        col1, col2, col3 = st.columns([1, 2, 1],
                                  vertical_alignment='center')
        with col2:
            image = Image.open("media/images.png")
            st.image(image)
        st.header("Proyecto final Análisis de datos \[integrador]")
        st.page_link("app.py", label="Inicio")
        st.page_link("pages/procesamiento.py", label="Limpieza")
        st.page_link("pages/caudal.py", label="Caudal")
        st.page_link("pages/radiacion.py", label="Radiación")
        st.page_link("pages/viento.py", label="Viento")
        

        
    

# funcion del modelo predictivo

