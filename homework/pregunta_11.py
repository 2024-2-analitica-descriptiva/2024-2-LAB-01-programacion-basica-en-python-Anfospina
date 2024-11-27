"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    x11=open('files/input/data.csv').readlines()
    x11=[z.replace('\n',"") for z in x11]
    x11=[z.split("\t") for z in x11]
    key=[z[3] for z in x11[0:]]
    value=[int(z[1]) for z in x11[0:]]
    asignacion = {letra: [] for letra in 'abcdefg'}
    for grupo, numero in zip(key, value):
        letras = grupo.split(',')
        for letra in letras:
            asignacion[letra].append(numero)
    suma_asignacion = {letra: sum(valores) for letra, valores in asignacion.items()}
    return suma_asignacion
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
if __name__ == "__main__":
    print(pregunta_11())