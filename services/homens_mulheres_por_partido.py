import streamlit as st
import pandas as pd
import altair as alt

def homens_mulheres_por_partido(df):
	if 'SG_PARTIDO' not in df.columns or 'CD_GENERO' not in df.columns:
			st.error("O arquivo não contém as colunas necessárias ('SG_PARTIDO' ou 'CD_GENERO').")
	else:
			# Agrupa os dados por partido e gênero
			genero_partido = df.groupby(['SG_PARTIDO', 'CD_GENERO']).size().reset_index(name='Contagem')

			# Mapeia 1 para homens e 2 para mulheres, assumindo que 'CD_GENERO' segue essa convenção
			genero_partido['Gênero'] = genero_partido['CD_GENERO'].map({1: 'Homens', 2: 'Mulheres'})

			# Criar o gráfico de torres lado a lado com Altair
			st.subheader("Gráfico de Torres - Homens e Mulheres por Partido")
			chart = alt.Chart(genero_partido).mark_bar().encode(
					x=alt.X('SG_PARTIDO:N', title='Partido', sort='-y'),  # Partido no eixo x
					y=alt.Y('Contagem:Q', title='Número de Pessoas'),  # Contagem no eixo y
					color=alt.Color('Gênero:N', title='Gênero'),  # Colore por gênero (Homens/Mulheres)
					tooltip=['SG_PARTIDO', 'Gênero', 'Contagem']
			).properties(
					title='Distribuição de Homens e Mulheres por Partido',  # Título do gráfico
					width=600,  # Largura do gráfico
					height=400   # Altura do gráfico
			)

			# Exibir o gráfico
			st.altair_chart(chart, use_container_width=True)