"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    x3=open('files/input/data.csv').readlines()
    x3=[z.replace('\n',"") for z in x3]
    x3=[z.replace('\t',",") for z in x3]
    x3=[z.split(",") for z in x3]
    key=[z[0] for z in x3[0:]]
    value=[int(z[1]) for z in x3[0:]]
    dic = {}
    for k, v in zip(key, value):
        if k in dic:
            dic[k].append(v)
        else:
            dic[k] = [v]
    resultado=sorted([(k,max(v),min(v)) for k,v in dic.items()])
    return resultado
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
if __name__ == "__main__":
    print(pregunta_05())