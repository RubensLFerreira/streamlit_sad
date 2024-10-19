import streamlit as st
import pandas as pd
import altair as alt

def mulher_por_partido(df):
	if 'SG_PARTIDO' not in df.columns or 'CD_GENERO' not in df.columns:
			st.error("O arquivo não contém as colunas necessárias ('SG_PARTIDO' ou 'CD_GENERO').")
	else:
			mulheres_df = df[df['CD_GENERO'] == 2]  
			mulheres_por_partido = mulheres_df['SG_PARTIDO'].value_counts().reset_index()
			mulheres_por_partido.columns = ['Partido', 'Número de Mulheres']
			mulheres_por_partido = mulheres_por_partido.sort_values(by='Número de Mulheres', ascending=False)

			st.subheader("Gráfico de Torres - Mulheres por Partido")
			chart = alt.Chart(mulheres_por_partido).mark_bar().encode(
					x=alt.X('Partido:N', title='Partido', sort='-y'),  
					y=alt.Y('Número de Mulheres:Q', title='Número de Mulheres'),  
					tooltip=['Partido', 'Número de Mulheres']
			).properties(
					title='Número de Mulheres por Partido', 
					width=600,  
					height=400   
			)

			st.altair_chart(chart, use_container_width=True)