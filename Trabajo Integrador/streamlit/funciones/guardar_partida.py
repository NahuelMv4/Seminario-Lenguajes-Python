import json
import pandas as pd
from pathlib import Path

def comparar (partida):
    return partida['puntaje']

def guardar(partida_actual):
    path_partidas = Path('./users/partidas.json')
    if path_partidas.exists():
        with open(path_partidas, 'r', encoding='UTF-8') as file:
            partidas = json.load(file)
    else:
        partidas = []
    # Agrego la partida actual ordenadamente
    df_ord = sorted(partidas + [partida_actual], key=comparar, reverse=True)
    
    # Devuelvo posicion.
    pos = df_ord.index(partida_actual)
    
    # Lo escribo en el archivo
    with path_partidas.open('w', encoding='UTF-8') as file:
        json.dump(df_ord, file, indent=4, ensure_ascii=False)
    return pos
