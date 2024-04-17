
import streamlit as st

# Configuración de la página en modo ancho
st.set_page_config(layout="wide")

# Título de la aplicación
st.title('Recomendador de Juegos')

# Simulación de algunos juegos
juegos = {
    'Aventura': [('Juego de Aventura 1', 2004), ('Juego de Aventura 2', 2010)],
    'Estrategia': [('Juego de Estrategia 1', 2008), ('Juego de Estrategia 2', 2015)],
    'Puzzle': [('Juego de Puzzle 1', 2012), ('Juego de Puzzle 2', 2017)]
}

# Expander para información sobre la app
with st.expander('Acerca de este juego'):
    st.write("""
        Esta aplicación recomienda juegos basados en el género, rango de años, clasificación por edad y nombre seleccionados por el usuario.
        Utiliza datos simulados y es solo un ejemplo de cómo puedes estructurar tu aplicación Streamlit.
    """)
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# Entrada de datos en la barra lateral
st.sidebar.header('Entrada de Datos')
genero = st.sidebar.selectbox('Elige el género del juego:', ['', 'Aventura', 'Estrategia', 'Puzzle'])
año_inicio, año_fin = st.sidebar.slider('Selecciona el rango de años:', 2000, 2024, (2010, 2020))
clasificacion_edad = st.sidebar.selectbox('Selecciona la clasificación por edad:', ['', 'Para todos', 'Mayores de 7', 'Mayores de 13', 'Mayores de 18'])
nombre_juego = st.sidebar.text_input('Buscar por nombre de juego:')
nuevo_juego = st.sidebar.text_input('Añadir nuevo juego:')
ver_todos = st.sidebar.checkbox('Ver todos los juegos')
eliminar_juego = st.sidebar.selectbox('Eliminar juego:', ['', *sum(juegos.values(), [])])

# Lógica para recomendar juegos basada en la entrada
def obtener_recomendaciones(genero, año_inicio, año_fin, clasificacion, nombre):
    recomendaciones = []
    for key, value in juegos.items():
        if genero == key or genero == '' or genero is None:
            for nombre_juego, año in value:
                if nombre in nombre_juego and (año_inicio <= año <= año_fin) and (clasificacion in nombre_juego or clasificacion == ''):
                    recomendaciones.append((nombre_juego, año))
    return recomendaciones

# Output de recomendaciones
st.header('Recomendaciones de Juegos')
if ver_todos:
    st.write('Todos los juegos:')
    for key, value in juegos.items():
        for nombre_juego, año in value:
            st.write(f"**{nombre_juego}** ({año})")
else:
    recomendaciones = obtener_recomendaciones(genero, año_inicio, año_fin, clasificacion_edad, nombre_juego)
    if recomendaciones:
        for juego, año in recomendaciones:
            st.write(f"**{juego}** ({año})")
    else:
        st.write("No se encontraron juegos que coincidan con los criterios.")

# Agregar nuevo juego a la lista
if nuevo_juego:
    # Agregar nuevo juego a la lista
    if nuevo_juego:
        genero_nuevo = st.selectbox('Selecciona el género del nuevo juego:', ['', *juegos.keys()])
        año_nuevo = st.number_input('Ingresa el año del nuevo juego:', value=2024, step=1)
        if st.button('Agregar nuevo juego'):
            if genero_nuevo and año_nuevo:
                juegos.setdefault(genero_nuevo, []).append((nuevo_juego, año_nuevo))
                st.write(f"Nuevo juego '{nuevo_juego}' añadido al género '{genero_nuevo}'")
            else:
                st.write("Por favor, selecciona un género y proporciona el año del nuevo juego.")

# Eliminar juego de la lista
if eliminar_juego:
    for key, value in juegos.items():
        if eliminar_juego in value:
            juegos[key].remove(eliminar_juego)
            st.write(f"Juego '{eliminar_juego[0]}' eliminado de la lista de juegos.")

# Otra funcionalidad (Ejemplo: Calcular el promedio de años de los juegos)
if ver_todos:
    años = [año for _, año in sum(juegos.values(), [])]
    promedio = sum(años) / len(años)
    st.write(f"El promedio de años de los juegos es: {promedio}")
