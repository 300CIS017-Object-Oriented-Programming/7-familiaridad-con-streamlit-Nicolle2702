import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('input')
nombre_jugador = st.sidebar.text_input('¿Cuál es tu nombre?')
icono_jugador = st.sidebar.selectbox('Elige un ícono', ['', '🎮', '🕹️', '🎲', '🃏', '🎯'])
juego_preferido = st.sidebar.selectbox('¿Cuál es tu juego favorito?', ['', 'Zelda', 'Mario Bros', 'Fortnite', 'Minecraft', 'Among Us'])

st.header('Resultados')

col1, col2, col3 = st.columns(3)

with col1:
  if nombre_jugador != '':
    st.write(f'👋 ¡Hola {nombre_jugador}!')
  else:
    st.write('👈 ¡Por favor ingresa tu **nombre**!')

with col2:
  if icono_jugador != '':
    st.write(f'{icono_jugador} es tu **ícono** favorito!')
  else:
    st.write('👈 ¡Por favor elige un **ícono**!')

with col3:
  if juego_preferido != '':
    st.write(f'🎮 **{juego_preferido}** es tu juego favorito!')
  else:
    st.write('👈 ¡Por favor elige tu juego favorito!')