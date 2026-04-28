import streamlit as st

st.title('Teste ECMI 2')
st.write("Esse é o meu texto")

nome = st.text_input('Digite o seu nome')
if nome:
    print(nome, 'é um cara legal!')

st.image('https://github.com/josircg/projeto1/blob/main/praia.webp')
