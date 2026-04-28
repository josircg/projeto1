import streamlit as st

st.title('Teste ECMI 2')
st.write("Esse é o meu texto")

nome = st.text_input('Digite o seu nome')
if nome:
    st.write(nome, 'é um cara legal!')

st.image('https://raw.githubusercontent.com/josircg/projeto1/refs/heads/main/praia.webp')
