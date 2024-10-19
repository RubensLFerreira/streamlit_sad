import streamlit as st
import pandas as pd
import altair as alt

def distribuicao_homem_mulher(df):  
	if 'CD_GENERO' not in df.columns:
			st.error("O arquivo não contém a coluna necessária ('CD_GENERO').")
	else:
			homem_mulher_count = df['DS_GENERO'].value_counts().reset_index()
			homem_mulher_count.columns = ['Homem/Mulher', 'Count']

			st.subheader("Gráfico de Pizza - Distribuição de Homem/Mulher dos Candidatos")
			chart = alt.Chart(homem_mulher_count).mark_arc(innerRadius=90).encode(
					theta=alt.Theta(field='Count', type='quantitative', title='Contagem'),
					color=alt.Color(field='Homem/Mulher', type='nominal', title='Homem/Mulher', legend=alt.Legend(title='Homem/Mulher')),
					tooltip=['Homem/Mulher', 'Count']
			).properties(
					title='Distribuição de Homens e Mulheres dos Candidatos',  
					width=400,  
					height=400   
			)

			st.altair_chart(chart, use_container_width=True)