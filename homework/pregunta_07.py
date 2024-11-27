"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    x7=open('files/input/data.csv').readlines()
    x7=[z.replace('\n','') for z in x7[0:]]
    x7=[z.replace('\t',',') for z in x7[0:]]
    x7=[z.split(',') for z in x7[0:]]
    key=[int(z[1]) for z in x7[0:]]
    value=[(z[0]) for z in x7[0:]]
    dic={}
    for k,v in zip(key,value):
        if k in dic:
            dic[k].append(v)
        else:
            dic[k]=[v]
    resultado=sorted(dic.items())
    return resultado
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
if __name__ == "__main__":
    print(pregunta_07())