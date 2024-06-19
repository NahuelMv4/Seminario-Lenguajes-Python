import streamlit as st

# Menú
with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        if st.button("Home"):
            st.switch_page("01_🏠Home.py")

    with col2:
        if st.button("Data"):
            st.switch_page("pages/02_📓Data.py")

    with col3:
        if st.button("Game"):
            st.switch_page("pages/03_🎮Game.py")

    with col4:
        if st.button("Registration Form"):
            st.switch_page("pages/04_📝Registration Form.py")

    with col5:
        if st.button("Ranking"):
            st.switch_page("pages/05_🥇Ranking.py")

    with col6:
        if st.button("Stats"):
            st.switch_page("pages/06_📊Stats.py")

# Título de la página
st.title('PyTrivia - Página de Inicio')

# Descripción del juego
st.header('¡Bienvenido a PyTrivia!')
st.write('PyTrivia es un juego de preguntas y respuestas donde podrás poner a prueba tus conocimientos en diferentes áreas.')

# Datos necesarios para comenzar a jugar
st.header('Comienza a Jugar')
st.write('Para comenzar a jugar, simplemente selecciona la sección de preguntas y elige la dificultad deseada.')

# Instrucciones básicas para jugar
st.header('Instrucciones de Juego')
st.write('1. Selecciona una categoría de preguntas.')
st.write('2. Elige la dificultad de las preguntas.')
st.write('3. Responde las preguntas correctamente para acumular puntos.')

# Explicación del funcionamiento del parámetro dificultad
st.header('Funcionamiento de la Dificultad')
st.write('El parámetro de dificultad te permite seleccionar el nivel de desafío de las preguntas. Puedes elegir entre Fácil, Medio y Difícil.')
st.write('Fácil: se le brindan tres respuestas de las cuales una es la correcta')
st.write('Medio: se le informa la cantidad de letras de la respuesta.')
st.write('Difícil: no se brindan ayudas.')

# Información de los integrantes
tab1, tab2, tab3 = st.columns(3)

with tab1:
    st.header('Información del Integrante 1')
    st.subheader('Nombre Completo')
    st.write('Felipe Di Plácido')
    st.subheader('Legajo')
    st.write('21256/2')

with tab2:
    st.header('Información del Integrante 2')
    st.subheader('Nombre Completo')
    st.write('Franco Darío Ramírez')
    st.subheader('Legajo')
    st.write('22063/9')

with tab3:
    st.header('Información del Integrante 3')
    st.subheader('Nombre Completo')
    st.write('Nahuel Saroglia Gambino')
    st.subheader('Legajo')
    st.write('25447/6')
