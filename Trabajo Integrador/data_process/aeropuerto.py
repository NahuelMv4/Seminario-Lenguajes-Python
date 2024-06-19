def elevation_name(line):
    """
        El proceso recibe una linea del archivo ar-airports.csv.
        Convierte los ft (line[6]) en integer para poder ser comparados,
        en caso de que ft no tenga valor alguno su 'elevation_name'
        es igual de nulo.
        Luego compara ft con los valores dados por el punto para ser asignado a su
        respectivo valor.
        Retorna la linea con el agregado del valor correspondiente para la
        columna 'elevation_name'.
    """
    ft = int(line[6]) if line[6] != '' else '' 
    if ft== '':
        line.append('')
    elif ft <= 131:
        line.append('bajo')
    elif ft <= 903:
        line.append('medio')
    else:
        line.append('alto')


def prov_name(reader_prov, line):
    """
        Recibe como parametros el reader del archivo de provincias para
        ser recorrido, y una linea del archivo ar-airports para ser modificado.
        Declaramos variable found para ser utilizada como corte dentro del while proximo.
        Dentro del while toma una linea del archivo provincias, y llama a la funcion simple_text.
        La funcion simple_text devuelve en city y en muny lo pasado como parametro en minuscua y sin tildes.
        comparo ambas variables, en caso de ser iguales a la linea de ar-airports sera agregado la provincia que
        le corresponde. En caso de que nunca encuentre un igual se le asignara un ''.
        Retorna la linea modificada.
    """
    next(reader_prov) #LEE EL HEADER
    found= False
    while found == False:
        try:
            line_prov= next(reader_prov)
            city = simple_text(line_prov[0])
            muni = simple_text(line[13])
            if city == muni:
                line.append(line_prov[5])
                found = True
        except StopIteration:
            line.append('')
            found= True


def simple_text(str):
    """
        Recibe un string.
        Primero llevamos a minuscula el string y luego eliminamos todas las tildes.
        Retorna el string pero en minusculas y sin tildes.
    """
    special_char = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'
    }
    minus= str.lower()
    text= ''.join(special_char.get(char, char) for char in minus)
    return text