"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    x=open('files/input/data.csv').readlines()
    x=[z.replace('\n',"") for z in x]
    x=[z.replace('\t',",") for z in x]
    x=[z.split(",") for z in x]
    x=[int(z[1]) for z in x[0:]]
    
    return sum(x) 
    
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
if __name__ == "__main__":
    print(pregunta_01())