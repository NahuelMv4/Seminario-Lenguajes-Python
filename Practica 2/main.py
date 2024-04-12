import Modules

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, 
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, 
Francsica, FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

# Generar estadísticas asociadas a cada jugador o jugadora
estadisticas_jugadores = Modules.generarEstructura(names, goals, goals_avoided, assists)

# Obtener el nombre y la cantidad de goles del goleador o goleadora
nombre_goleador, goles_goleador = Modules.goleador(estadisticas_jugadores)

# Obtener el nombre del jugador más influyente
nombre_influyente = Modules.jugadorMasInfluyente(estadisticas_jugadores)

# Obtener el promedio de goles por partido del equipo en general
promedio_goles_equipo = Modules.promedioDeGolesPorPartidoEquipo(sum(goals))

# Obtener el promedio de goles por partido del goleador o goleadora
promedio_goles_goleador = Modules.promedioDeGolesPorPartidoGoleador(goles_goleador)

# Imprimir los resultados
print("Nombre del goleador:", nombre_goleador)
print("Cantidad de goles del goleador:", goles_goleador)
print("Nombre del jugador mas influyente:", nombre_influyente)
print("Promedio de goles por partido del equipo en general:", promedio_goles_equipo)
print("Promedio de goles por partido del goleador:", promedio_goles_goleador)