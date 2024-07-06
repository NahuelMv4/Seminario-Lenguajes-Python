import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import matplotlib.pyplot as plt
from funciones.cargar_partidas import cargar_partidas

# Funciones de los incisos proporcionados
def jugadores_por_genero(df_users, df_partidas):
    # Se filtran los usuarios que han jugado al menos una vez
    usuarios_que_jugaron = df_partidas['mail'].unique()
    df_usuarios_jugadores = df_users[df_users['mail'].isin(usuarios_que_jugaron)]

    # Se cuenta el número de jugadores por género
    conteo_por_genero = df_usuarios_jugadores['gen'].value_counts()

    # Se genera el gráfico de torta
    fig_genero = px.pie(conteo_por_genero, values=conteo_por_genero.values, names=conteo_por_genero.index, title="Jugadores por agrupados por género")

    st.plotly_chart(fig_genero)

    st.write('---')

def partidas_superior_media(df_partidas):
    # Se calcula la media de puntos
    puntuacion_media = df_partidas['puntaje'].mean()

    # se agregan las partidas con puntaje superior a la media
    df_partidas['superior_a_media'] = df_partidas['puntaje'] > puntuacion_media

    # Se cuentan estas partidas
    conteo_partidas = df_partidas['superior_a_media'].value_counts()

    # Se cambian los índices para mostrar en el gráfico
    conteo_partidas.index = conteo_partidas.index.map({True: 'Superiores a la Media', False: 'Iguales o Inferiores a la Media'})

    # Se genera el gráfico de torta
    fig_partidas = px.pie(conteo_partidas, values=conteo_partidas.values, names=conteo_partidas.index, title="Porcentaje de partidas con puntuación superior a la media")
    st.plotly_chart(fig_partidas)

    st.write('---')

def partidas_por_dia_de_semana(df_partidas):
    # Se convierte la columna 'hora'(str) a datetime
    df_partidas['hora'] = pd.to_datetime(df_partidas['hora'])

    # Se agrega el día de la semana para cada partida con propiedad de Datetime
    df_partidas['dia_semana'] = df_partidas['hora'].dt.day_name()

    # Se cuenta el número de partidas por día de la semana
    conteo_por_dia = df_partidas['dia_semana'].value_counts().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # Se genera el gráfico de barras para partidas por día de la semana
    fig_dia_semana = px.bar(conteo_por_dia, x=conteo_por_dia.index, y=conteo_por_dia.values,
                            labels={'x': 'Día de la Semana', 'y': 'Cantidad de Partidas'},
                            title='Cantidad de Partidas por Día de la Semana')

    st.plotly_chart(fig_dia_semana)

    st.write('---')

def promedios_aciertos_mensuales(df_partidas):
    st.subheader("Promedio de preguntas acertadas mensualmente")

    # Se fija una fecha de incio default
    fecha_inicio_default = pd.Timestamp('2024-01-01')

    # Se establecen selección de fechas
    fecha_inicio = st.date_input("Fecha de inicio", value=fecha_inicio_default, key='fecha_inicio_inciso4')
    fecha_fin = st.date_input("Fecha de fin", value=pd.to_datetime('today'), key='fecha_fin_inciso4')

    # Se verifica si se han seleccionado ambas fechas
    if fecha_inicio and fecha_fin:

        # Se convierten las fechas en objetos Timestamp para luego poder comparar
        fecha_inicio = pd.Timestamp(fecha_inicio)
        fecha_fin = pd.Timestamp(fecha_fin) + pd.Timedelta(days=1)
        
        # Se filtran las partidas dentro del rango de fechas seleccionado
        df_partidas_filtradas = df_partidas[
            (pd.to_datetime(df_partidas['hora']) >= fecha_inicio) & 
            (pd.to_datetime(df_partidas['hora']) < fecha_fin)
        ] 

        # Se verifica si hay partidas en el rango de fechas seleccionado
        if not df_partidas_filtradas.empty:

            # Se convierte la columna 'hora'(str) a tipo Datetime y se establece como índice
            df_partidas_filtradas['fecha'] = pd.to_datetime(df_partidas_filtradas['hora'])
            df_partidas_filtradas.set_index('fecha', inplace=True)
            
            # Se calcula el promedio mensual de preguntas acertadas
            # Resample('M'): agrupa de manera mensual
            promedio_mensual = df_partidas_filtradas['cant correctas'].resample('M').mean()

            # Se formatea la fecha para que solo se muestre el mes y año
            promedio_mensual.index = promedio_mensual.index.strftime('%Y-%m')

            # Se genera el gráfico de líneas del promedio mensual
            st.table(promedio_mensual)

        else:
            st.write("No hay partidas en el rango de fechas seleccionado.")
    else:
        st.write("Seleccione un rango de fechas para continuar.")

    st.write('---')

def top10_rango_fechas(df_partidas):
    st.subheader('Top 10 acumulado')

    # Se establecen fechas por defecto
    fecha_inicio_default = pd.to_datetime('2024-01-02')
    fecha_fin_default = pd.to_datetime('today')

    # Se establecen selección de fecha con valores por defecto
    fecha_inicio = st.date_input("Fecha de inicio", value=fecha_inicio_default, key='fecha_inicio_inciso5')
    fecha_fin = st.date_input("Fecha de fin", value=fecha_fin_default, key='fecha_fin_inciso5')

    # Se verifica si las fechas de inicio y fin son válidas
    if fecha_inicio and fecha_fin:
    
        # Se convierten las fechas en objetos Timestamp
        fecha_inicio = pd.Timestamp(fecha_inicio)
        fecha_fin = pd.Timestamp(fecha_fin) + pd.Timedelta(days=1)
        
        # Se filtran las partidas dentro del rango de fechas seleccionado
        df_partidas_filtradas = df_partidas[
            (pd.to_datetime(df_partidas['hora']) >= fecha_inicio) & 
            (pd.to_datetime(df_partidas['hora']) < fecha_fin)
        ]

    # Se asegura de que hay datos para calcular el top 10
    if not df_partidas_filtradas.empty:
        # Se calcula la cantidad de puntos acumulados por cada usuario
        puntos_acumulados = df_partidas_filtradas.groupby('user')['puntaje'].sum().reset_index()

        # Se ordenan los usuarios por la cantidad de puntos acumulados y se selecciona el top 10 con mayores puntajes
        top_10_usuarios = puntos_acumulados.sort_values(by='puntaje', ascending=False).head(10)

        # Se genera el gráfico de barras para el top 10 de usuarios por puntos acumulados
        fig_top_10 = px.bar(top_10_usuarios, x='user', y='puntaje',
                            labels={'user': 'Usuario', 'puntaje': 'Puntos Acumulados'},
                            title='Top 10 de Usuarios con Mayor Cantidad de Puntos Acumulados')

        st.plotly_chart(fig_top_10)
    else:
        st.write("No hay partidas en el rango de fechas seleccionado.")

    st.write('---')

# Inciso 6 
def ordenar_datasets_por_errores(partidas):
    # Definir las rutas de los archivos CSV
    ruta_lagos = Path('../custom_data/lagos_arg.csv')
    ruta_aeropuertos = Path('../custom_data/ar-airports-custom.csv')
    ruta_censo = Path('../custom_data/c2022_tp_c_resumen_adaptado_custom.csv')
    ruta_conectividad = Path('../custom_data/Conectividad_internet_modificado.csv')

    # Crear un diccionario para almacenar las rutas de los archivos
    rutas_archivos = {
        "Lagos": ruta_lagos,
        "Aeropuertos": ruta_aeropuertos,
        "Censo 2022": ruta_censo,
        "Conectividad": ruta_conectividad
    }

    # Crear un diccionario para almacenar la cantidad total de errores por temática
    cant_errores = {
        "Lagos": 0,
        "Aeropuertos": 0,
        "Conectividad": 0,
        "Censo 2022": 0
    }

    # Iterar sobre las filas del DataFrame y calcular los errores por temática
    for index, row in partidas.iterrows():
        try:
            # Convertir cant_correctas a entero
            cant_correctas = int(row['cant correctas'])
            cant_preguntas = 5
            errores = cant_preguntas - cant_correctas
            tematica = row['tematica']

            # Sumar los errores al contador correspondiente en cant_errores
            if tematica == "Lagos":
                cant_errores["Lagos"] += errores
            elif tematica == "Aeropuertos":
                cant_errores["Aeropuertos"] += errores
            elif tematica == "Conectividad":
                cant_errores["Conectividad"] += errores
            elif tematica == "Censo 2022":
                cant_errores["Censo 2022"] += errores

        except ValueError as e:
            st.warning(f"Error al convertir 'cant correctas' a entero en la fila {index}: {e}")

    # Crear un DataFrame a partir de cant_errores para mostrar los resultados
    df_errores = pd.DataFrame(list(cant_errores.items()), columns=['Tematica', 'Cantidad de Errores'])
    
    # Ordenar el DataFrame por la cantidad de errores de forma descendente
    df_errores = df_errores.sort_values(by='Cantidad de Errores', ascending=False)
    
    return df_errores

# Inciso 7
def grafico_evolucion_puntaje(df, usuario1, usuario2):
    df['hora'] = pd.to_datetime(df['hora'])
    df_usuario1 = df[df['user'] == usuario1].sort_values(by='hora')
    df_usuario2 = df[df['user'] == usuario2].sort_values(by='hora')
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_usuario1['hora'], df_usuario1['puntaje'], label=usuario1, marker='o')
    plt.plot(df_usuario2['hora'], df_usuario2['puntaje'], label=usuario2, marker='o')
    
    plt.xlabel('Hora')
    plt.ylabel('Puntaje')
    plt.title('Evolución del puntaje')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Inciso 8
def listar_tematica_por_genero(df_users, df_partidas):
    df_users['username'] = df_users['username'].str.strip()
    df_combinado = pd.merge(df_partidas, df_users, left_on='user', right_on='username')
    
    df_combinado['conocimiento'] = df_combinado['cant correctas'] / 5
    
    mejor_tematica_por_genero = df_combinado.groupby(['gen', 'tematica']).agg({'conocimiento': 'mean'}).reset_index()
    idx = mejor_tematica_por_genero.groupby(['gen'])['conocimiento'].idxmax()
    return mejor_tematica_por_genero.loc[idx][['gen', 'tematica']]

# Inciso 9
def listar_puntaje_promedio_por_dificultad(df):
    return df.groupby('dificultad').agg(puntaje_promedio=('puntaje', 'mean'), veces_elegida=('dificultad', 'size')).reset_index()

# Inciso 10
def listar_usuarios_en_racha(df):
    df['hora'] = pd.to_datetime(df['hora'])
    ultima_semana = df[df['hora'] >= (pd.Timestamp.now() - pd.Timedelta(days=7))]
    # Se filtra por los usuarios que tienen en la última semana todas sus partidas con puntaje mayor a 0
    racha_usuarios = ultima_semana.groupby('user').filter(lambda x: (x['puntaje'] > 0).all())

    # Se filtra por los usuarios que jugaron los últimos 7 dias 
    usuarios_en_racha = racha_usuarios.groupby('user').filter(lambda x: x['hora'].dt.date.nunique() == 7)
    return usuarios_en_racha['user'].unique()

# Cargar datos
try:
    partidas = cargar_partidas()
    df_partidas = pd.DataFrame(partidas)
except FileNotFoundError as e:
    st.error(f"Error: {e}") 
except ValueError as e:
    st.error(f"Error: {e}")

# Se obtienen los usuarios con manejador de excepciones
path_users = Path('./users/users.json')
try:
    df_users = pd.read_json(path_users)
except FileNotFoundError:
    st.error(f"El archivo {path_users} no existe.")
except ValueError as e:
    st.error(f"Error al leer el archivo JSON: {e}")


st.title("📊 Estadísticas del Juego")
# Inciso 1
jugadores_por_genero(df_users, df_partidas)
# Inciso 2
partidas_superior_media(df_partidas)

# Inciso 3
partidas_por_dia_de_semana(df_partidas)

# Inciso 4
promedios_aciertos_mensuales(df_partidas)

# Inciso 5
top10_rango_fechas(df_partidas)

# Inciso 6
st.subheader("Datasets ordenados por número de errores")
st.table(ordenar_datasets_por_errores(df_partidas))

# Inciso 7
st.subheader("Comparación de evolución de puntaje entre dos usuarios")
usuarios = df_partidas['user'].unique()
usuario1 = st.selectbox('Selecciona el primer usuario', usuarios)
usuario2 = st.selectbox('Selecciona el segundo usuario', usuarios)
if st.button("Comparar usuarios"):
    grafico_evolucion_puntaje(df_partidas, usuario1, usuario2)

# Inciso 8
st.subheader("Temática con mayor conocimiento por género")
st.table(listar_tematica_por_genero(df_users, df_partidas))

# Inciso 9
st.subheader("Puntaje promedio por dificultad")
st.table(listar_puntaje_promedio_por_dificultad(df_partidas))

# Inciso 10
st.subheader("Usuarios en racha")
st.table(listar_usuarios_en_racha(df_partidas))
