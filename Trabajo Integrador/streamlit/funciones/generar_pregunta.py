import random
import pandas as pd
from pathlib import Path


def mezclar_diccionario(diccionario):
    # Convertir el diccionario en una lista de pares (clave, valor)
    items = list(diccionario.items())

    # Mezclar la lista de pares de manera aleatoria
    random.shuffle(items)

    # Crear un nuevo diccionario a partir de la lista mezclada
    diccionario_mezclado = dict(items)
    return diccionario_mezclado


def procesar_diccionario(diccionario):
    # Convertir el diccionario en una lista de pares (clave, valor)
    items = list(diccionario.items())

    # Tomar las tres primeras claves con sus valores
    primeras_tres = items[:3]

    # Tomar la cuarta clave
    pregunta = items[3][0]

    respuesta = items[3][1]

    return primeras_tres, pregunta, respuesta


def generar_pregunta(ruta, filas, respuesta=None):
    df = pd.read_csv(ruta)
    df_reducido = df.loc[:, filas]

    # Eliminar filas con cualquier valor nulo en las columnas seleccionadas
    df_reducido = df_reducido.dropna()

    if respuesta == None:
        fila_aleatoria = df_reducido.sample(n=1)
        diccionario = {fila: fila_aleatoria[fila].values[0] for fila in filas}

        diccionario = mezclar_diccionario(diccionario)
        atributos, pregunta, respuesta = procesar_diccionario(diccionario)
        return [atributos, pregunta, respuesta]

    #Cuando recibe respuesta se ejucta este codigo.
    else:
        ops = respuesta
        while (ops == respuesta):
            ops = df_reducido.sample(n=1).values[0]
        return ops



def obtener_pregunta (tematica):
    match tematica:
        case 'Aeropuertos':
            csv_file = Path('../custom_data/ar-airports-custom.csv')
            filas = ['type', 'name', 'municipality', 'elevation_name']
            dict_atributos, pregunta, respuesta = generar_pregunta(csv_file, filas)
        case 'Lagos':
            csv_file = Path('../custom_data/lagos_arg.csv')
            filas = ['Nombre', 'Ubicación', 'Superficie (km2)', 'Sup Tamaño']
            dict_atributos, pregunta, respuesta = generar_pregunta(csv_file, filas)
        case 'Conectividad':
            csv_file = Path('../custom_data/Conectividad_internet_modificado.csv')
            filas = ['Provincia', 'Partido', 'Localidad', 'posee_conectividad']
            dict_atributos, pregunta, respuesta = generar_pregunta(csv_file, filas)
        case 'Censo 2022':
            csv_file = Path('../custom_data/c2022_tp_c_resumen_adaptado_custom.csv')
            filas = ['Jurisdicción', 'Total de población', 'Población en situación de calle(²)', 'Porcentaje de población en situación de calle']
            dict_atributos, pregunta, respuesta = generar_pregunta(csv_file, filas)

    return dict_atributos, pregunta, respuesta

def ayuda_facil (tematica, pregunta, respuesta):
    """
    El proceso recibita la tematica para indagar segun esta, el nombre de la fila para elegir otra respuesta de esta misma,
    y la respuesta para no devolver la misma respuesta en ops
    """
    match tematica:    
        case 'Aeropuertos':
            csv_file = Path('../custom_data/ar-airports-custom.csv')
            ops = generar_pregunta(csv_file, pregunta, respuesta)
            ops2 = generar_pregunta(csv_file, pregunta, respuesta)
        case 'Lagos':
            csv_file = Path('../custom_data/lagos_arg.csv')
            ops = generar_pregunta(csv_file, pregunta, respuesta)
            ops2 = generar_pregunta(csv_file, pregunta, respuesta)
        case 'Conectividad':
            csv_file = Path('../custom_data/Conectividad_internet_modificado.csv')
            ops = generar_pregunta(csv_file, pregunta, respuesta)
            ops2 = generar_pregunta(csv_file, pregunta, respuesta)
        case 'Censo 2022':
            csv_file = Path('../custom_data/c2022_tp_c_resumen_adaptado_custom.csv')
            ops = generar_pregunta(csv_file, pregunta, respuesta)
            ops2 = generar_pregunta(csv_file, pregunta, respuesta)
    return ops, ops2
