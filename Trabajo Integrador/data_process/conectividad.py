def reemplazar_valores(fila):
    """
    Reemplaza los valores '--' por 'NO' en una fila del dataset.

    Args:
        fila: Lista que representa una fila del dataset.

    Retorna:
        None
    """
    for i, valor in enumerate(fila):
        if valor == "--":
            fila[i] = "NO"

def tiene_conectividad(fila):
    """
    Determina si una fila posee conectividad.

    Args:
        fila: Lista que representa una fila del dataset.

    Retorna:
        Un String 'SI' si la fila posee al menos un tipo de conectividad, 'NO' en caso contrario.
    """
    conectividad = fila[4:13]  # Tomar solo los campos relevantes
    for dato in conectividad:
        if dato != "NO":
            return "SI"
    return "NO"
