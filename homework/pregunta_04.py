"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter

def pregunta_04():
    x4=open('files/input/data.csv').readlines()
    x4=[z.replace('\n',"") for z in x4]
    x4=[z.replace('\t',",") for z in x4]
    x4=[z.split(",") for z in x4]
    mes=[z[2].split("-")[1] for z in x4[0:]]
    return sorted(Counter(mes).items())
    
    
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
if __name__ == "__main__":
    print(pregunta_04())