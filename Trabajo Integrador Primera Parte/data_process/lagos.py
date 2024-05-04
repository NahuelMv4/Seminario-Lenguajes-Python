def convertir_coordenadas(latitud_gms, longitud_gms):
    """ 
    Convierte las coordenadas de grados, minutos y segundos a grados decimales.

    Args:
    - latitud_gms (str): Coordenada de latitud en formato de grados, minutos y segundos.
    - longitud_gms (str): Coordenada de longitud en formato de grados, minutos y segundos.

    Returns:
    - tuple: Una tupla que contiene la latitud y longitud en grados decimales.
    """
    separar_coordenadas = lambda coordenada: coordenada.replace("°", " ").replace("'", " ").replace("\"", " ").split()
   
    latitud_gms = separar_coordenadas (latitud_gms)
    longitud_gms = separar_coordenadas (longitud_gms)
    
    convertir_a_grados_decimales = lambda grados, minutos, segundos, direccion: (grados + minutos / 60 + segundos / 3600 )* (-1 if direccion in ['S', 'O'] else 1)

    latitud_gd = convertir_a_grados_decimales (float(latitud_gms[0]), float(latitud_gms[1]), float(latitud_gms[2]), latitud_gms[3])
    longitud_gd = convertir_a_grados_decimales (float(longitud_gms[0]), float(longitud_gms[1]), float(longitud_gms[2]), longitud_gms[3])

    return latitud_gd, longitud_gd



def calcular_sup_tamaño(superficie=None):
    """
    Calcula el tamaño de un lago en función de su superficie.

    Args:
    - superficie (float): Superficie del lago en kilómetros cuadrados.

    Returns:
    - str: Clasificación del tamaño del lago (chico, medio, grande).
    """
    SUP_CHICA = 17
    SUP_MEDIA = 59

    if superficie <= SUP_CHICA:
        return 'chico'
    elif superficie <= SUP_MEDIA:
        return 'medio'
    else:
        return 'grande' 
    
