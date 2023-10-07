import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar o layout da página
st.set_page_config(layout="wide")

# Carregar os dados do arquivo "vendas.csv" (certifique-se de que o arquivo está no mesmo diretório)
df = pd.read_csv("vendas.csv", sep=";", decimal=",")

# Converter a coluna "Date" para o formato de data
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Criar uma nova coluna "Month" que contém o ano e o mês
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Criar uma seleção de meses na barra lateral do dashboard
month = st.sidebar.selectbox("Mês", df["Month"].unique())
df_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2)  # Primeira linha com duas colunas
col3, col4, col5 = st.columns(3)  # Segunda linha com três colunas

# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")

# Exibir o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)

# Criar o gráfico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h")

# Exibir o gráfico na segunda coluna
col2.plotly_chart(fig_prod, use_container_width=True)

# Calcular o faturamento total por cidade
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()

# Criar o gráfico de barras para exibir o faturamento por cidade
fig_city = px.bar(city_total, x="City", y="Total",
                   title="Faturamento por cidade")

# Exibir o gráfico na terceira coluna
col3.plotly_chart(fig_city, use_container_width=True)

# Criar o gráfico de pizza para exibir o faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                   title="Faturamento por tipo de pagamento")

# Exibir o gráfico na quarta coluna
col4.plotly_chart(fig_kind, use_container_width=True)

# Calcular a avaliação média por cidade
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()

# Criar o gráfico de barras para exibir a avaliação média
fig_rating = px.bar(df_filtered, y="Rating", x="City",
title="Avaliação Média")

# Exibir o gráfico na quinta coluna
col5.plotly_chart(fig_rating, use_container_width=True)
