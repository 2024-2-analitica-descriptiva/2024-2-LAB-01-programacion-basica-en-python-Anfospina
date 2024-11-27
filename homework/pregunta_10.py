"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    x10=open('files/input/data.csv').readlines()
    x10=[z.replace('\n',"") for z in x10]
    x10=[z.split("\t") for z in x10]
    key=[z[0] for z in x10[0:]]
    value1=[z[3].split(',') for z in x10[0:]]
    value2=[z[4].split(',') for z in x10[0:]]
    lista=[]
    for k,v1,v2 in zip(key,value1,value2):
            t=(k,len(v1),len(v2))
            lista.append(t)
    return lista
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
if __name__ == "__main__":
    print(pregunta_10())