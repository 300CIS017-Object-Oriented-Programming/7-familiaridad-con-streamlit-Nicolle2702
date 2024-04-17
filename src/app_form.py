import streamlit as st

st.title('st.form')


st.header('uso de la notación `with`')
st.subheader('Misión de rescate')

with st.form('mi_misión'):
    st.write('**Completa tu misión**')


    tipo_arma_val = st.selectbox('Arma principal', ['Espada', 'Arco', 'Varita mágica'])
    armadura_val = st.selectbox('Tipo de armadura', ['Pesada', 'Ligera', 'Mágica'])
    habilidad_val = st.selectbox('Habilidad especial', ['Teletransporte', 'Invisibilidad', 'Control mental'])
    mascota_val = st.selectbox('Mascota compañera', ['Dragón', 'Lobo', 'Fénix'])
    nivel_val = st.select_slider('Nivel de experiencia', ['Novato', 'Intermedio', 'Experto'])
    mision_completada_val = st.checkbox('Misión completada')


    enviado = st.form_submit_button('Enviar')

if enviado:
    st.markdown(f'''
        🎮 Has completado la misión:
        - Arma principal: `{tipo_arma_val}`
        - Armadura: `{armadura_val}`
        - Habilidad especial: `{habilidad_val}`
        - Mascota compañera: `{mascota_val}`
        - Nivel de experiencia: `{nivel_val}`
        - Misión completada: `{mision_completada_val}`
        ''')
else:
    st.write('☝️ ¡Cumple tu misión!')


st.header('2. Ejemplo de notación de objeto')

formulario = st.form('mi_formulario_2')
valor_seleccionado = formulario.slider('Selecciona un nivel')
formulario.form_submit_button('Enviar')

st.write('Nivel seleccionado: ', valor_seleccionado)
