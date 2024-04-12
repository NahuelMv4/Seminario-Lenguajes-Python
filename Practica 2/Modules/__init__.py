# 1. Generar una estructura todas las estadísticas asociadas a cada jugador o jugadora.
def generarEstructura(names, goals, goals_avoided, assists):
    """
    Genera un diccionario con las estadísticas asociadas a cada jugador o jugadora utilizando la función zip.
    
    Argumentos:
    - names: Cadena de texto con los nombres de los jugadores separados por coma y espacio.
    - goals: Lista con la cantidad de goles de cada jugador.
    - goals_avoided: Lista con la cantidad de goles evitados de cada jugador.
    - assists: Lista con la cantidad de asistencias de cada jugador.
    
    Retorna:
    - Diccionario donde las claves son los nombres de los jugadores y los valores son diccionarios con las estadísticas asociadas a cada jugador.
    """
    estadisticas_jugadores = {}
    for nombre, goles, goles_evitados, asistencias in zip(names.split(", "), goals, goals_avoided, assists):
        estadisticas_jugadores[nombre] = {'Goles': goles, 'Goles Evitados': goles_evitados, 'Asistencias': asistencias}
    return estadisticas_jugadores

# 2. Conocer el nombre y la cantidad de goles del goleador o goleadora.
def goleador(estadisticas_jugadores):
    """
    Devuelve el nombre y la cantidad de goles del goleador o goleadora.
    
    Argumentos:
    - estadisticas_jugadores: Diccionario con las estadísticas asociadas a cada jugador.
    
    Retorna:
    - Una tupla que contiene el nombre del goleador o goleadora y la cantidad de goles.
    """
    max_goles = max(estadisticas_jugadores.values(), key=lambda x: x['Goles'])
    return list(estadisticas_jugadores.keys())[list(estadisticas_jugadores.values()).index(max_goles)], max_goles['Goles']

# 3. Conocer el nombre del jugador o jugadora más influyente
def jugadorMasInfluyente(estadisticas_jugadores):
    """
    Devuelve el nombre del jugador o jugadora más influyente.
    
    Argumentos:
    - estadisticas_jugadores: Diccionario con las estadísticas asociadas a cada jugador.
    
    Retorna:
    - El nombre del jugador o jugadora más influyente.
    """
    max_influencia = max(estadisticas_jugadores.values(), key=lambda x: 1.5 * x['Goles'] + 1.25 * x['Goles Evitados'] + x['Asistencias'])
    return list(estadisticas_jugadores.keys())[list(estadisticas_jugadores.values()).index(max_influencia)]

# 4. Conocer el promedio de goles por partido del equipo en general.
def promedioDeGolesPorPartidoEquipo(goles_totales):
    """
    Calcula el promedio de goles por partido del equipo en general.
    
    Argimentos:
    - goles_totales: Cantidad total de goles anotados por el equipo.
    
    Retorna:
    - El promedio de goles por partido del equipo en general.
    """
    partidos_jugados = 25
    return goles_totales / partidos_jugados

# 5. Conocer el promedio de goles por partido del goleador o goleadora.
def promedioDeGolesPorPartidoGoleador(goles_goleador):
    """
    Calcula el promedio de goles por partido del goleador o goleadora.
    
    Argumentos:
    - goles_goleador: Cantidad de goles del goleador o goleadora.
    
    Retorna:
    - El promedio de goles por partido del goleador o goleadora.
    """
    partidos_jugados = 25
    return goles_goleador / partidos_jugados