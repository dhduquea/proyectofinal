import streamlit as st
import utilidades as util
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd

def generarMenu():
    with st.sidebar:
        image = Image.open("media\images.png")
        st.image(image)
        st.header("Proyecto final Análisis de datos \[integrador]")
        st.page_link("app.py", label="Inicio")
        st.page_link("pages/procesamiento.py", label="Limpieza")
        st.page_link("pages/caudal.py", label="Caudal")
        st.page_link("pages/radiacion.py", label="Radiación")
        st.page_link("pages/viento.py", label="Viento")
        

        
    

# funcion del modelo predictivo

