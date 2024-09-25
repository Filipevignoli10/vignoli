import pandas as pd
import streamlit as st

# Carregar o arquivo Excel
file_path = r'C:\Users\filip\Desktop\PDF\tste.xlsx'
df = pd.read_excel(file_path)

# Configurar layout da página para largura máxima
st.set_page_config(layout="wide")

# Título da aplicação
st.title('REDE AUXILIAR')

# Centralizar e estilizar o campo de pesquisa
st.markdown(
    """
    <style>
    .centered-input {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra de pesquisa centralizada
with st.container():
    search_term = st.text_input('Pesquisar na tabela:', key='search', max_chars=50)

# Filtrar o dataframe com base no termo de pesquisa
if search_term:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
else:
    filtered_df = df

# Mostrar o dataframe filtrado
st.dataframe(filtered_df)