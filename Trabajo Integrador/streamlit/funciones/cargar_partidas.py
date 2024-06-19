from pathlib import Path
import pandas as pd

def cargar_partidas():
    path_partidas = Path('./users/partidas.json')
    df_partidas = pd.read_json(path_partidas)
    return df_partidas
