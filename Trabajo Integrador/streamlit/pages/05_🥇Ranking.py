import streamlit as st
import pandas as pd
import sys
from pathlib import Path
import json

sys.path.append(str(Path('..').resolve()))
from funciones import guardar_partida

# En caso de que sea redireccionado desde una partida terminada.
if "ranking_state" in st.session_state:
    st.title("📄 Tu última partida")
    st.markdown(f':gray[ •  Usted ha respondido correctamente {st.session_state.ranking_state["correct"]} de 5 preguntas]')
    st.markdown(f':gray[ •  Su puntaje total es de {st.session_state.ranking_state["score"]}]')
    st.markdown(f':gray[ •  En el ranking histórico has quedado en {st.session_state.ranking_state["pos"]+1} posición.]')

    # Todas las list_quest y sus respuestas.
    for i in range(5):
        with st.container(border=True):
            st.title(f"Pregunta :blue[{i+1}]")
            for clave, atributo in st.session_state.ranking_state["list_quest"][i]["datos"]:
                st.write(f":gray[{clave}: {atributo}]")
            st.markdown(f'La pregunta es sobre: {st.session_state.ranking_state["list_quest"][i]["pregunta"]}')
            st.markdown(f':green[Respuesta Correcta:] {st.session_state.ranking_state["list_quest"][i]["r_correcta"]}')
            if str(st.session_state.ranking_state["list_quest"][i]["r_correcta"]).lower() == str(st.session_state.ranking_state["list_quest"][i]["r"]).lower():
                st.markdown(f':green[Respuesta del usuario:] {st.session_state.ranking_state["list_quest"][i]["r"]}')
            else:
                st.markdown(f':red[Respuesta del usuario:] {st.session_state.ranking_state["list_quest"][i]["r"]}')
    if st.button('Borrar Historial'):
        del st.session_state.ranking_state
        st.rerun()

# Ranking historico, se muestra en ambos casos.
with st.container():
    
    path_users = Path('./users/partidas.json')
    df = pd.read_json(path_users)
    col= ['user','puntaje','mail']
    nuevos_nombres= {
        'user' : 'Usuario',
        'mail' : 'Correo Electronico',
        'puntaje': 'Puntaje'
    }
    df_reducido = df[col]
    df_reducido.rename(columns=nuevos_nombres, inplace=True)
    st.title("Ranking Histórico")

    # Muestro solo top 15, y columnas user, puntaje y mail.
    st.write(df_reducido.head(15))

