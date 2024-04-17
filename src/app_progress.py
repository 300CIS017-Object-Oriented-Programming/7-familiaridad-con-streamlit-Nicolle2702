

import streamlit as st
import time

st.title('st.progress')

with st.expander('Acerca de este juego'):
    st.write('¡Ahora puedes ver el progreso de tu aventura en este juego con el comando `st.progreso`!')

mi_barra = st.progress(0)

for porcentaje_completo in range(100):
    time.sleep(0.05)
    mi_barra.progress(porcentaje_completo + 1)

st.balloons()
