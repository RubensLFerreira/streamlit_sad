import streamlit as st
import pandas as pd
import altair as alt

def distribuicao_por_grau_intrucao(df):
  if 'DS_GENERO' not in df.columns or 'DS_GRAU_INSTRUCAO' not in df.columns:
      st.error("O arquivo não contém as colunas necessárias ('DS_GENERO', 'DS_GRAU_INSTRUCAO').")
  else:
      genero_grau_count = df.groupby(['DS_GENERO', 'DS_GRAU_INSTRUCAO']).size().reset_index(name='count')

      st.subheader("Gráfico de Barras - Gênero vs Grau de Instrução (Lado a Lado)")
      chart = alt.Chart(genero_grau_count).mark_bar().encode(
          x=alt.X('DS_GRAU_INSTRUCAO:N', title='Grau de Instrução'), 
          y=alt.Y('count:Q', title='Contagem'), 
          color='DS_GENERO:N', 
          tooltip=['DS_GRAU_INSTRUCAO', 'DS_GENERO', 'count']  
      ).properties(
          title='Distribuição de Gênero por Grau de Instrução',  
          width=500,  
          height=400   
      ).configure_axis(
          labelFontSize=12,
          titleFontSize=14
      ).configure_legend(
          labelFontSize=12
      )

      st.altair_chart(chart, use_container_width=True)