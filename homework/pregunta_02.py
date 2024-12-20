"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter

def pregunta_02():
    lista=open('files/input/data.csv').readlines()
    lista=[z.replace('\n',"") for z in lista]
    lista=[z.replace('\t',",") for z in lista]
    lista=[z.split(",") for z in lista]
    lista=[z[0] for z in lista[0:]]
    lista=sorted(Counter(lista).items())
    return lista
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
if __name__ == "__main__":
    print(pregunta_02())