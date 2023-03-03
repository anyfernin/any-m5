import streamlit as st
import pandas as pd

st.title("Caso Netflix")
st.write("Equipo 5")
sidebar = st.sidebar
sidebar.title("Barra de opciones")
sidebar.write("Seleccione filtros deseados")



Data_URL="movies.csv"
import codecs
@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data_load_state=st.text("Loading data...")
data=load_data(500)
data_load_state.text("Done...")

if sidebar.checkbox("Show dataframe"):
    st.dataframe(data)

Titulo=sidebar.text_input("Titulo del filme:")
btnTitulo=sidebar.button("Buscar filmes")
if (btnTitulo):
    data_Titulo=data.copy()
    data_Titulo["name"]=data_Titulo["name"].str.lower()
    filterbyrange=data_Titulo[data_Titulo["name"].str.contains(Titulo.lower())]
    count_row=filterbyrange.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyrange)

Director = sidebar.selectbox("Seleccionar director:", data['director'].unique())
btnDirector=sidebar.button("Filtrar director")
if (btnDirector):
    filterbyDir=data[data["director"]==Director]
    count_row=filterbyDir.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyDir)
