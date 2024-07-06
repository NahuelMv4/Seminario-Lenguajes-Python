from pathlib import Path
import pandas as pd

def cargar_partidas():
    """
    Carga un DataFrame de un archivo JSON.

    La función intenta cargar un archivo JSON ubicado en './users/partidas.json' 
    y convertirlo en un DataFrame de pandas. Si el archivo no se encuentra, 
    lanza una excepción FileNotFoundError. Si hay un error al leer el archivo 
    JSON, lanza una excepción ValueError.

    Returns:
        pd.DataFrame: Un DataFrame que contiene los datos del archivo JSON.

    Raises:
        FileNotFoundError: Si el archivo JSON no existe.
        ValueError: Si hay un error al leer el archivo JSON.
    """
    path_partidas = Path('./users/partidas.json')
    
    try:
        df_partidas = pd.read_json(path_partidas)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {path_partidas} no existe.")
    except ValueError as e:
        raise ValueError(f"Error al leer el archivo JSON: {e}")
    
    return df_partidas
