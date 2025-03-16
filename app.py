import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('/vehicles.csv', sep=',')  # lendo os dados

# convertendo a coluna price para float
df['price'] = df['price'].astype(float)

# convertendo a coluna date_posted para datetime
df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')

df['model_year'] = df['model_year'].fillna(
    0)  # preenchendo os valores nulos com 0
# convertendo a coluna model_year para int
df['model_year'] = df['model_year'].astype(int)

df['cylinders'] = df['cylinders'].fillna(
    0)  # preenchendo os valores nulos com 0
# convertendo a coluna cylinders para int
df['cylinders'] = df['cylinders'].astype(int)

df['odometer'] = df['odometer'].fillna(0)  # preenchendo os valores nulos com 0
# convertendo a coluna odometer para float
df['odometer'] = df['odometer'].astype(float)

# preenchendo os valores nulos com 'unknown'
df['paint_color'] = df['paint_color'].fillna('unknown')

df['is_4wd'] = df['is_4wd'].fillna(0)  # preenchendo os valores nulos com 0
# convertendo a coluna is_4wd para boolean
df['is_4wd'] = df['is_4wd'].astype(bool)

st.header('Análise de dados de anúncios de vendas de carros')  # título

hist_button = st.button('Criar histograma')  # criar um botão
if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(df, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão')  # criar um botão
if disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.scatter(df, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
