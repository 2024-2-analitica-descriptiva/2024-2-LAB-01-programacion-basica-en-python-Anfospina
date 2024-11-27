"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter

def pregunta_09():
    x9=open('files/input/data.csv').readlines()
    x9=[z.replace('\n',"") for z in x9]
    x9=[z.split("\t") for z in x9]
    x9=[z[4].split(',') for z in x9[0:]]
    lista=[]
    for sublista in x9:
        for item in sublista:
            key,value = item.split(":")
            lista.append(key)

    dic=Counter(lista)
    dic=dict(sorted(dic.items()))
    return dic
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
if __name__ == "__main__":
    print(pregunta_09())