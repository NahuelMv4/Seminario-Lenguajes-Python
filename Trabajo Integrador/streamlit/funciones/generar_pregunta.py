import random
import pandas as pd
from pathlib import Path


def mezclar_diccionario(diccionario):
    """
    Esta funcion mezcla de manera aleatoria los elementos de un diccionario.

    Args:
        diccionario (dict): El diccionario a mezclar.

    Returns:
        diccionario (dict): Un nuevo diccionario con los elementos mezclados.
    """
    # Se convierte el diccionario en una lista de pares(clave, valor)
    items = list(diccionario.items())

    # Se mezcla la lista de pares de manera aleatoria
    random.shuffle(items)

    # Se crea un nuevo diccionario a partir de la lista mezclada
    diccionario_mezclado = dict(items)
    return diccionario_mezclado


def procesar_diccionario(diccionario):
    """
    Esta funcion procesa un diccionario tomando las tres primeras entradas(atributos) y separando la cuarta clave(pregunta) y su valor(respuesta correcta).

    Args:
        diccionario (dict): El diccionario a procesar.

    Returns:
        tuple: Una tupla que contiene:
            - list: Los tres primeros atributos como pares (clave, valor).
            - str: La cuarta clave, que es la pregunta.
            - any: La respuesta correspondiente a pregunta.
    """

    # Se convierte el diccionario en una lista de pares (clave, valor)
    items = list(diccionario.items())

    # Se toman las tres primeras claves con sus valores
    primeras_tres = items[:3]

    # Se toma la cuarta clave
    pregunta = items[3][0]

    # Se toma el cuarto valor
    respuesta = items[3][1]

    return primeras_tres, pregunta, respuesta

def reducir_df(ruta, columnas):
    df = pd.read_csv(ruta)
    df_reducido = df[columnas].copy()

    # Se elimanan filas con cualquier valor nulo en las columnas seleccionadas
    df_reducido = df_reducido.dropna()

    return df_reducido


def generar_pregunta(ruta, columnas):
    """
    Esta función genera una pregunta a partir de un archivo CSV y las columnas seleccionadas, haciendo uso de pandas.

    Args:
        ruta (Path): La ruta al archivo CSV.
        filas (list): Las columnas a seleccionar del CSV.
        respuesta (any, optional): La respuesta para la validación, por defecto es None.

    Returns:
        list: Una lista que contiene:
            - list: Tres primeros atributos como pares (columna, valor).
            - str: El nombre de la columna seleccionada como pregunta.
            - any: El valor correspondiente a la columna seleccionada como respuesta.
    """
    df_reducido = reducir_df (ruta, columnas)

    # Se toma una fila aleatoria del dataframe
    fila_aleatoria = df_reducido.sample(n=1)

    # Se toman los datos de la fila aleatoria
    diccionario = {columna: fila_aleatoria[columna].values[0] for columna in columnas}

    diccionario = mezclar_diccionario(diccionario)
    atributos, pregunta, respuesta = procesar_diccionario(diccionario)

    return [atributos, pregunta, respuesta]



def obtener_ayuda_facil(ruta, pregunta, respuesta):
    df_reducido = reducir_df(ruta, pregunta)

    ops = respuesta
    while (ops == respuesta):
        ops = df_reducido.sample(n=1).values[0]
    return ops



def obtener_pregunta (tematica):
    """
    Esta funcion obtiene una pregunta según en la temática seleccionada.

    Args:
        tematica (str): La temática para la cual se desea generar la pregunta.

    Returns:
        tuple: Una tupla que contiene:
            - list: Tres primeros atributos como pares (columna, valor).
            - str: El nombre de la columna seleccionada como pregunta.
            - str: El valor correspondiente a la columna seleccionada como respuesta.
    """
    match tematica:
        case 'Aeropuertos':
            csv_file = Path('../customdata/ar-airports-custom.csv')
            columnas = ['type', 'name', 'municipality', 'elevation_ft', 'elevation_name']
        case 'Lagos':
            csv_file = Path('../customdata/lagos_arg.csv')
            columnas = ['Nombre', 'Ubicación', 'Superficie (km2)', 'Profundidad máxima (m)', 'Sup Tamaño']
        case 'Conectividad':
            csv_file = Path('../customdata/Conectividad_internet_modificado.csv')
            columnas = ['Provincia', 'Partido', 'Localidad', 'Poblacion','posee_conectividad']
        case 'Censo 2022':
            csv_file = Path('../customdata/c2022_tp_c_resumen_adaptado_custom.csv')
            columnas = ['Jurisdicción', 'Total de población', 'Población en viviendas particulares', 'Población en situación de calle(²)', 'Porcentaje de población en situación de calle']
    
    dict_atributos, pregunta, respuesta = generar_pregunta(csv_file, columnas)
    return dict_atributos, pregunta, respuesta

def ayuda_facil (tematica, pregunta, respuesta):
    """
    El proceso recibita la tematica para indagar segun esta, el nombre de la fila para elegir otra respuesta de esta misma,
    y la respuesta para no devolver la misma respuesta en ops
    """
    match tematica:    
        case 'Aeropuertos':
            csv_file = Path('../customdata/ar-airports-custom.csv')
        case 'Lagos':
            csv_file = Path('../customdata/lagos_arg.csv')
        case 'Conectividad':
            csv_file = Path('../customdata/Conectividad_internet_modificado.csv')
        case 'Censo 2022':
            csv_file = Path('../customdata/c2022_tp_c_resumen_adaptado_custom.csv')

    ops = obtener_ayuda_facil(csv_file, pregunta, respuesta)
    ops2 = obtener_ayuda_facil(csv_file, pregunta, respuesta)
    return ops, ops2

