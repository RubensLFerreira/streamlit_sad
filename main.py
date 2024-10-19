import streamlit as st
import pandas as pd

from services.previa_informacoes import previa_informacoes
from services.distribuicao_por_grau_intrucao import distribuicao_por_grau_intrucao
from services.distribuicao_por_cor_raca import distribuicao_por_cor_raca
from services.distribuicao_homem_mulher import distribuicao_homem_mulher
from services.mulher_por_partido import mulher_por_partido
from services.homens_mulheres_por_partido import homens_mulheres_por_partido

st.title("Prévia dos dados dos candidatos das eleições de 2024")

uploaded_files = st.file_uploader(
    "Escolha um arquivo CSV", type="csv", accept_multiple_files=True
)

if uploaded_files is not None:
  try:
      for uploaded_file in uploaded_files:
          df = pd.read_csv(uploaded_file, encoding='ISO-8859-1', sep=';')

          previa_informacoes(df)
          distribuicao_por_grau_intrucao(df)
          distribuicao_por_cor_raca(df)
          distribuicao_homem_mulher(df)
          mulher_por_partido(df)
          homens_mulheres_por_partido(df)

  except Exception as e:
      st.error(f"Erro ao processar o arquivo: {str(e)}")
