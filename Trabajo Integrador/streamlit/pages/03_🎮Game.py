import streamlit as st
import json
import sys
import random
import pandas as pd
from datetime import datetime
from pathlib import Path

sys.path.append(str(Path('..').resolve()))
from funciones import generar_pregunta, guardar_partida

# NO_CREADO -> GENERAR_PREGUNTA -> NUEVO -> MOSTRAR_PUNTAJE
#                      ^---------------------------v

# 1. El juego tiene estados.
# 2. Los datos que quiero persistir los guardo en el session_state.
# 3. Cada vez que cambio de estado ejecuto rerun() para volver a ejecutar
#    el script.

# Si no existe el estado, lo creo
if ("game_state" not in st.session_state):
    st.session_state["game_state"] = {
        "state": "NO_CREADO",
        "user": None,
        "mail": "",
        "score": 0,
        "respuesta_correcta" : None,
        "ultima_respuesta": '',
        "ultima_pregunta": "",
        "ultimas_opciones": [],
        "ultimas_ayudas": [],
        "tematica": None,
        "dificultad": None,
        "cantidad_preguntas": 0,
        "cant_correctas": 0,
        "preguntas": []
    }
    
    

if st.session_state.game_state["state"] == "NO_CREADO":

    # OBTENER USUARIOS
    path_users = Path('./users/users.json')
    df = pd.read_json(path_users)

    opciones_usuarios = [f"{row['username']} ({row['mail']})" for _,row in df.iterrows()]
    
    tematicas = ['Aeropuertos', 'Lagos', 'Conectividad', 'Censo 2022']
    dificultades = ["Fácil", "Media", "Difícil"]

    st.title(":blue[Inicio del Juego]")

    # SELECCIONAR USUARIO, TEMATICA Y DIFICULTAD
    with st.form("user_selection"):
        nombre = st.selectbox('Usuario', opciones_usuarios,placeholder='Seleccione su usuario', index= None)
        tematica = st.selectbox('Temática', tematicas,placeholder='Seleccione la temática', index= None)
        dificultad = st.selectbox('Dificultad', dificultades,placeholder='Seleccione la dificultad', index= None)
        jugar = st.form_submit_button("Jugar")
    if jugar:
        
        # Primero consulto si todas las opciones han sido rellenadas.
        if nombre != None and tematica != None and dificultad != None:
            st.session_state.game_state["state"] = "GENERAR_PREGUNTA"
            st.session_state.game_state["user"], st.session_state.game_state["mail"] = nombre.split(' ')
            st.session_state.game_state["tematica"] = tematica
            st.session_state.game_state["dificultad"] = dificultad
            st.rerun()
        else:
            st.error('Ingrese todos los campos')

    if st.button("¿Quieres registrarte?"):
        st.switch_page("pages/04_📝Registration Form.py")

# Proceso intermedio entre pregunta y pregunta.
elif st.session_state.game_state["state"] == "GENERAR_PREGUNTA":
    if st.session_state.game_state["cantidad_preguntas"] < 5:
        st.session_state.game_state["cantidad_preguntas"] += 1
        st.session_state.game_state["state"] = "NUEVO"
        tematica = st.session_state.game_state['tematica']
        dificultad = st.session_state.game_state['dificultad']

        # Llamo a mi funcion obtener_pregunta y seteo en ultimas_opciones, ultima_pregunta y respuesta_correcta sus respectivos
        # valores.
        st.session_state.game_state["ultimas_opciones"], st.session_state.game_state["ultima_pregunta"], st.session_state.game_state["respuesta_correcta"]= generar_pregunta.obtener_pregunta(tematica)
        
        match st.session_state.game_state["dificultad"]:
            case "Fácil":

                # Genero 2 baiteos con los cuales voy a rellenar mis opciones a elegir. Utilizo la funcion ayuda_facil.
                baits1, baits2 = generar_pregunta.ayuda_facil(st.session_state.game_state["tematica"], st.session_state.game_state["ultima_pregunta"], st.session_state.game_state["respuesta_correcta"])
                st.session_state.game_state["ultimas_ayudas"] = [st.session_state.game_state["respuesta_correcta"], baits1, baits2]
                
                # Hago una copia de la lista con mis 3 valores (2 errorenos, 1 correcto) para no perder estos valores originales
                # al momento de hacer random.shuffle, con el cual aleatorizo la lista entre sus 3 elementos.
                opciones = list(st.session_state.game_state["ultimas_ayudas"])
                random.shuffle(opciones)
                st.session_state.game_state["ultimas_ayudas"] = opciones
            case "Media":

                # Asigno a mi variable state una lista con cada char de la respuesta correcta.
                st.session_state.game_state["ultimas_ayudas"] = list(str(st.session_state.game_state["respuesta_correcta"]))
    else:

        # Si ya mostre las 5 preguntas en hora de mostrar mi puntaje.
        st.session_state.game_state["state"] = "MOSTRAR_PUNTAJE"
    st.rerun()

elif st.session_state.game_state["state"] == "NUEVO":
    with st.form("questions"):
        pregunta = st.session_state.game_state["ultima_pregunta"]
        atributos = st.session_state.game_state["ultimas_opciones"]
        num_pregunta = st.session_state.game_state["cantidad_preguntas"]

        # MUESTRO PREGUNTA
        st.title(f"Pregunta :blue[{num_pregunta}] de :blue[5]")
        for clave, atributo in atributos:
            st.write(f":gray[{clave}: {atributo}]")
        st.write(f"{pregunta}:")
        # Segun la dificultad elegida se mostraran las ayudas.
        match st.session_state.game_state["dificultad"]:
            case "Fácil":

                # Muestro las opciones para la opcion facil.
                st.markdown(f":green[Ayuda Fácil activada]")
                respuesta = st.selectbox(f"{pregunta}", st.session_state.game_state["ultimas_ayudas"],placeholder="Elija su respuesta" ,index= None)
            case "Media":

                # Asigno de ayuda la cantidad de letras que tiene la respuesta.
                ayuda = len(st.session_state.game_state["ultimas_ayudas"])
                st.markdown(f":orange[Ayuda Media activada]")
                st.markdown(f"La palabra tiene  :orange[{ayuda}]  letras")
                respuesta = st.text_input(f"{pregunta}", placeholder="Ingrese su respuesta", value="")
            case "Difícil":

                # No hay ayuda.
                respuesta = st.text_input(f"{pregunta}", placeholder= "Ingrese su respuesta", value= '')
        responder = st.form_submit_button("Enviar")
    if responder:

        # Verifico si se ha seleccionado una respuesta.
        if respuesta != None and respuesta != '':
            st.session_state.game_state['ultima_respuesta'] = respuesta

            # Guardo la pregunta, la respuesta y la respuesta correcta.
            nueva_pregunta= {
                "pregunta": pregunta,
                "datos" : atributos,
                "r_correcta": st.session_state.game_state["respuesta_correcta"],
                "r": st.session_state.game_state["ultima_respuesta"]
            }
            st.session_state.game_state["preguntas"].append(nueva_pregunta)
            st.session_state.game_state["state"] = "GENERAR_PREGUNTA"

            # SUMAR SEGUN DIFICULTAD
            if str(st.session_state.game_state["ultima_respuesta"]).lower() == str(st.session_state.game_state["respuesta_correcta"]).lower():
                st.session_state.game_state["cant_correctas"] += 1 
                match st.session_state.game_state["dificultad"]:
                    case "Fácil":
                        st.session_state.game_state["score"] += 1
                    case "Media":
                        st.session_state.game_state["score"] += 1.5
                    case "Difícil":
                        st.session_state.game_state["score"] += 2
            st.rerun()
        else:
            st.error('Elija una respuesta')


# State final del game.
elif st.session_state.game_state["state"] == "MOSTRAR_PUNTAJE":
    st.markdown(f"Has :green[respondido correctamente {st.session_state.game_state['cant_correctas']}] de 5")
    st.markdown(f"En la dificultad {st.session_state.game_state['dificultad']}")
    st.markdown(f"En la tematica {st.session_state.game_state['tematica']}")
    st.markdown(f"Has logrado conseguir :blue[{st.session_state.game_state['score']} puntos]")
    
    # De esta forma no ocurre el doble guardado.
    if 'partida_guardada' not in st.session_state:
        st.session_state.partida_guardada = False

    if not st.session_state.partida_guardada:
        # Se guarda la partida actual
        partida_actual = {
            'user': st.session_state.game_state["user"],
            'mail': st.session_state.game_state["mail"].strip('()'),
            'hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'dificultad': st.session_state.game_state["dificultad"],
            'tematica': st.session_state.game_state["tematica"],
            'cant correctas': st.session_state.game_state["cant_correctas"],
            'puntaje' : st.session_state.game_state["score"]
        } 
        pos = guardar_partida.guardar(partida_actual)

        # Session_state para enviar a mi pagina ranking.
        st.session_state["ranking_state"] = {
            'user' : st.session_state.game_state["user"],
            'mail' : st.session_state.game_state["mail"],
            'score' : st.session_state.game_state["score"],
            'list_quest' : st.session_state.game_state["preguntas"],
            'correct' : st.session_state.game_state["cant_correctas"],
            'pos' : pos
        }   
        st.session_state.partida_guardada = True

    if st.button("Ver Ranking"):

        # Eliminino mi state del game, toda mi informacion necesario esta guardada en el JSON y el ranking_state.
        # Borro para asi al volver a esta pagina poder reingresar a jugar directamente.
        del st.session_state.game_state
        st.session_state.partida_guardada = False
        st.switch_page("pages/05_🥇Ranking.py")
