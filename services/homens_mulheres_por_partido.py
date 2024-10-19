import streamlit as st
import pandas as pd
import altair as alt

def homens_mulheres_por_partido(df):
	if 'SG_PARTIDO' not in df.columns or 'CD_GENERO' not in df.columns:
			st.error("O arquivo não contém as colunas necessárias ('SG_PARTIDO' ou 'CD_GENERO').")
	else:
			genero_partido = df.groupby(['SG_PARTIDO', 'CD_GENERO']).size().reset_index(name='Contagem')
			genero_partido['Gênero'] = genero_partido['CD_GENERO'].map({1: 'Homens', 2: 'Mulheres'})

			st.subheader("Gráfico de Torres - Homens e Mulheres por Partido")
			chart = alt.Chart(genero_partido).mark_bar().encode(
					x=alt.X('SG_PARTIDO:N', title='Partido', sort='-y'),  
					y=alt.Y('Contagem:Q', title='Número de Pessoas'), 
					color=alt.Color('Gênero:N', title='Gênero'),  
					tooltip=['SG_PARTIDO', 'Gênero', 'Contagem']
			).properties(
					title='Distribuição de Homens e Mulheres por Partido',  
					width=600,  
					height=400   
			)

			st.altair_chart(chart, use_container_width=True)