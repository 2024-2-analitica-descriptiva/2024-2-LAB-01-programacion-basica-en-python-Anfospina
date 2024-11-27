"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    x3=open('files/input/data.csv').readlines()
    x3=[z.replace('\n',"") for z in x3]
    x3=[z.replace('\t',",") for z in x3]
    x3=[z.split(",") for z in x3]
    key=[z[0] for z in x3[0:]]
    value=[int(z[1]) for z in x3[0:]]
    dic = {}
    for k, v in zip(key, value):
        if k in dic:
            dic[k] += v 
        else:
            dic[k] = v
    
    return sorted(dic.items())
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
if __name__ == "__main__":
    print(pregunta_03())