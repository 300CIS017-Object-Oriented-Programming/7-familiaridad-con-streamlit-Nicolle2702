
import streamlit as st

st.header('st.checkbox')

st.write ('Que te gustaria pedir?')

icecream = st.checkbox('Helado')
coffee = st.checkbox('Cafe')
cola = st.checkbox('Cola')

if icecream:
    st.write("Genial aqui tienes 🍦")

if coffee:
    st.write("Okay,Aca tienes cafe ☕")

if cola:
    st.write("Aqui esta 🥤")