import streamlit as st
import pandas as pd
import altair as alt

def previa_informacoes(df):   
	st.subheader(f"Candidatos do {df['SG_UF'].unique()[0]}")
	st.dataframe(df.head(), use_container_width=True)

	st.write(f"Total de linhas: {df.shape[0]}")
	st.write(f"Total de colunas: {df.shape[1]}")

	st.subheader("Distribuição por grau de instrução")
	st.write("Distribuição por Grau de Instrução")
	grau_instrucao_count = df.groupby('DS_GRAU_INSTRUCAO').size().reset_index(name='count')
	st.bar_chart(grau_instrucao_count.set_index('DS_GRAU_INSTRUCAO'), stack=False)