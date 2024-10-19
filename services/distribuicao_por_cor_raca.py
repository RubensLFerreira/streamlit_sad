import streamlit as st
import pandas as pd
import altair as alt

def distribuicao_por_cor_raca(df):   
	if 'CD_COR_RACA' not in df.columns:
			st.error("O arquivo não contém a coluna necessária ('CD_COR_RACA').")
	else:
			cor_raca_count = df['DS_COR_RACA'].value_counts().reset_index()
			cor_raca_count.columns = ['Cor/Raça', 'Count']

			st.subheader("Gráfico de Pizza - Distribuição de Cor/Raça dos Candidatos")
			chart = alt.Chart(cor_raca_count).mark_arc(innerRadius=90).encode(
					theta=alt.Theta(field='Count', type='quantitative', title='Contagem'),
					color=alt.Color(field='Cor/Raça', type='nominal', title='Cor/Raça', legend=alt.Legend(title='Cor/Raça')),
					tooltip=['Cor/Raça', 'Count']
			).properties(
					title='Distribuição de Cor/Raça dos Candidatos',  
					width=400,  
					height=400  
			)

			st.altair_chart(chart, use_container_width=True)