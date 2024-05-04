def esta_en_la_capital (municipio, csv_ar):
    """
    Comprueba si el municipio dado está en la capital según los datos proporcionados en el archivo CSV.

    Args:
        municipio (str): El nombre del municipio a verificar.
        csv_ar (iterable): El objeto iterable que contiene los datos de los municipios.

    Returns:
        boolean: True si el municipio está en la capital, False en caso contrario.
    """

    CITY = 0
    CAPITAL = 6

    #RECORRER EL ARCHIVO HASTA LLEGAR AL MUNICIPIO
    for city in csv_ar:
        ciudad = sin_tilde(city[CITY])
        if ciudad == municipio:
            if city[CAPITAL] in ['admin', 'primary']:
                return True

    return False


def sin_tilde (nombre):
    """
    Elimina los caracteres con tilde de una cadena de texto.

    Args:
        nombre (str): La cadena de texto que puede contener caracteres con tilde.

    Returns:
        str: La cadena de texto sin caracteres con tilde.
    """

    special_char = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u'
    }

    nombre = ''.join(special_char.get(char, char) for char in nombre)
    return nombre


def filtrar_provincias (provincias, poblacion, signo):
    """
    Filtra las provincias según la población y el signo especificados.

    Args:
        provincias (list): Lista de provincias con sus respectivas poblaciones.
        poblacion (int): Población de referencia para filtrar las provincias.
        signo (str): Signo de comparación ('>' o '<') para el filtrado de población.

    Returns:
        list: Lista de provincias que cumplen con el criterio de población especificado.
    """

    if signo == '>':
        return [provincia[0] for provincia in provincias if int(provincia[1]) > poblacion]
    else:
        return [provincia[0] for provincia in provincias if int(provincia[1]) < poblacion]


def actualizar_conectividad (localidad, provincia_a_actualizar):
    """
    Actualiza la conectividad de una provincia según los datos proporcionados por una localidad.

    Args:
        localidad (dict): Datos de la localidad con información de conectividad.
        provincia_a_actualizar (dict): Provincia que se actualizará según datos de la conectividad.

    Returns:
        None
    """

    for clave in provincia_a_actualizar.keys():
        if localidad[clave] == "SI" and provincia_a_actualizar[clave] == "NO":
            provincia_a_actualizar[clave] = "SI"


def obtener_lagos(provincias , csv_lagos):
    """
    Genera una lista de lagos que se encuentran dentro de las provincias especificadas.

    Args:
        provincias (list): Lista de provincias en las que se buscarán los lagos.
        csv_lagos (iterable): El objeto iterable que contiene los datos de los lagos.

    Returns:
        list: Lista de nombres de lagos que se encuentran dentro de las provincias especificadas.
    """

    lagos = []

    for lago in csv_lagos:

        if '/' in lago[1]:
            lago [1] = lago[1].split(' / ') 
            if lago[1][0] and lago[1][1] in provincias:     
                lagos.append (lago[0])

        elif lago[1] in provincias:
            lagos.append (lago[0])
    
    return lagos