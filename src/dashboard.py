# Dashboard em Streamlit - lê as views do PostgreSQL e mostra os gráficos
import pandas as pd
import plotly.express as px
import streamlit as st
from conexao import criar_conexao

engine = criar_conexao()


# Função para carregar dados de uma view
def carregar_dados(nome_view):
    return pd.read_sql(f"SELECT * FROM {nome_view}", engine)


st.title("Dashboard de Temperaturas IoT")
st.write("Dados de sensores de temperatura (Kaggle) guardados no PostgreSQL.")

# Gráfico 1: média de temperatura por dispositivo
st.header("Média de Temperatura por Dispositivo")
df_media = carregar_dados("avg_temp_por_dispositivo")
fig1 = px.bar(df_media, x="local", y="avg_temp", color="id_dispositivo",
              barmode="group",
              labels={"local": "Local do sensor", "avg_temp": "Temperatura média (°C)",
                      "id_dispositivo": "Dispositivo"})
st.plotly_chart(fig1)

# Gráfico 2: leituras por hora
st.header("Leituras por Hora do Dia")
df_hora = carregar_dados("leituras_por_hora")
fig2 = px.line(df_hora, x="hora", y="contagem",
               labels={"hora": "Hora do dia", "contagem": "Quantidade de leituras"})
st.plotly_chart(fig2)

# Gráfico 3: temperaturas máximas e mínimas por dia
st.header("Temperaturas Máximas e Mínimas por Dia")
df_dia = carregar_dados("temp_max_min_por_dia")
fig3 = px.line(df_dia, x="data", y=["temp_max", "temp_min"],
               labels={"data": "Data", "value": "Temperatura (°C)", "variable": "Medida"})
st.plotly_chart(fig3)
