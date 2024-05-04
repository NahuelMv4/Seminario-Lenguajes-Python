import streamlit as st
from pathlib import Path
import json

path = Path('./users/users.json')

st.header('👤 Panel de registro')

#Diccionario para guardar los datos a registrarse.
user_reg= {
        'username' : '',
        'name' : '',
        'mail' : '',
        'date' : None,
        'gen' : None
        }


with st.form ('my_form'):
    
    #Declaro los campos para ingresar la informacion, y los asigno a keys del dict anteriormente creado.
    user_reg['username'] = st.text_input('Usuario')
    user_reg['name'] = st.text_input('Nombre Completo')
    user_reg['mail'] = st.text_input('Correo Electronico')
    user_reg['date'] = str(st.date_input('Fecha de Nacimiento', value=None))
    user_reg['gen'] = st.selectbox('Genero', ['Masculino', 'Femenino', 'Otro'], index=None)

    #Al momento de hacer click en el boton "Registrarse" se activara el proceso de registrado.
    if st.form_submit_button('Registrarse'):

        #Primero verifico que se hayan rellenado todos los campos.
        if not(user_reg['username'] == '' or  user_reg['name'] == '' or user_reg['mail'] == '' 
               or user_reg['date'] == None or user_reg['gen'] == None):
            
            #Guardo mi archivo json con todos los usuario registrados en una variable.
            with path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            iterator = iter(data)
            found = False

            #Utilizo un iterador para recorrer la lista de diccionarios extraida del JSON.
            #Le paso como parametro "None", esto hara que al llegar al final de la lista se retorne None en user.
            user = next(iterator, None)
            while found != True and user != None:

                #Comparo el mail ingresado con el mail de cada usuario registrado.
                if user['mail'].lower() == user_reg['mail'].lower():

                    #En caso de encontrarse con un mail ya registrado actualizo toda su informacion con la nueva ingresada.
                    user['username'] = user_reg['username']
                    user['name'] = user_reg['name']
                    user['date'] = user_reg['date']
                    user['gen'] = user_reg['gen']
                    found = True
                user = next(iterator, None)
            
            #En caso de que no haya encontrado ningun mail registrado igual al ingresado solo es agregado al diccionario del archivo.
            if not found:
                data.append(user_reg)
                st.success('✅ Registrado correctamente')
            else:
                st.success('✅ Datos del usuario actualizados correctamente')
            
            #Escribo la variable data, con las modificaciones ya hechas, en el archivo JSON.
            with (path.open('w', encoding= 'utf-8')) as f:
                json.dump(data, f, indent=4)

        else:
            st.error('🚫 Complete todo los campos para registrarse')