

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'Cual es tu color favorito?',
     ('Azul', 'Rojo', 'Verde'))

st.write('Tu color favorito es: ', option)