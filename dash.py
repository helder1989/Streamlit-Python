# Importando os pacotes

import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image # manupulando imagem

@st.cache_data # traz maior velocidade ao lidar com big data
def gerar_df():
    df = pd.read_excel(
        io="dataset_anp.xlsx",
        engine="openpyxl",
        sheet_name="dataset_anp",
        usecols="A:Q", # colunas
        nrows=378079 # linhas
    )
    return df
df = gerar_df() # chamando a função que vai gerar o dataframe

