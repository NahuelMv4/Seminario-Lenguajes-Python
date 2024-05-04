import streamlit as st
tab1, tab2, tab3 = st.tabs(['Integrante 1', 'Integrante 2', 'Integrante 3'])
with tab1:
    st.header('Informacion del integrante')
    st.subheader('Nombre completo')
    st.write('Felipe Di Placido')

    st.subheader('Legajo')
    st.write('21256/2')
with tab2:
    st.header('Informacion del integrante')
    st.subheader('Nombre completo')
    st.write('Franco Dario Ramirez')

    st.subheader('Legajo')
    st.write('22063/9')
with tab3:
    st.header('Informacion del integrante')
    st.subheader('Nombre completo')
    st.write('Nahuel Saroglia Gambino')

    st.subheader('Legajo')
    st.write('25447/6')