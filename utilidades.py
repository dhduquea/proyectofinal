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
        col1, col2 = st.columns(2)
        with col1:
            image = Image.open("media\images.png")
            st.image(image)
        with col2:
            st.header("SMEC")

        st.page_link("app.py", label="Inicio")
        st.page_link("pages\limpieza.py", label="Pronostico")

# funcion del modelo predictivo

