import streamlit as st
import pandas as pd
import numpy as np

URL_DADOS_FARM_TOGETHER = 'https://raw.githubusercontent.com/lucasHashi/maximizacao-de-utilidade-farm-together/master/dados_completos.json'
URL_DADOS_FINAL_FARM_TOGETHER = 'https://raw.githubusercontent.com/lucasHashi/maximizacao-de-utilidade-farm-together/master/final.csv'

st.title('Hello Mundo, primeiro app Streamlit')

st.write('## Tabela final de recursos')

#df_dados_completos = pd.read_json(URL_DADOS_FARM_TOGETHER)
df_dados_final = pd.read_csv(URL_DADOS_FINAL_FARM_TOGETHER, sep='?')

st.write(df_dados_final)

st.write('## Mesma tabela, so que com filtro de colheita')

colheita_selecionada = st.selectbox('Colheitas',df_dados_final['tipo_colheita'].unique())
st.write(df_dados_final.loc[df_dados_final['tipo_colheita'] == colheita_selecionada])

st.sidebar.markdown('# Titulo da Sidebar')
st.sidebar.markdown('## Sub-Titulo da Sidebar')
st.sidebar.markdown('### Sub-Sub-Titulo da Sidebar')
opcao_sidebar = st.sidebar.selectbox('Sidebar Magica', ['opcao 1', 'item 2', 'magia 3'])
st.sidebar.markdown('Opção escolhida: '+str(opcao_sidebar))
slider_sidebar = st.sidebar.slider('Slider da Sidebar', 0, 100, (20,80))
slider_diferenca = slider_sidebar[1] - slider_sidebar[0]
st.sidebar.markdown('Range escolhido: {} - {}'.format(slider_sidebar[0], slider_sidebar[1]))
st.sidebar.markdown('Com a amplitude de: {}'.format(slider_diferenca))

# COMO USAR MAGIA
x = 4
x, 'quadrado é', x*x