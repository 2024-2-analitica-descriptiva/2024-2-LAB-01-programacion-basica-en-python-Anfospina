"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_08():
    x8=open('files/input/data.csv').readlines()
    x8=[z.replace('\n','') for z in x8[0:]]
    x8=[z.replace('\t',',') for z in x8[0:]]
    x8=[z.split(',') for z in x8[0:]]
    key=[int(z[1]) for z in x8[0:]]
    value=[(z[0]) for z in x8[0:]]
    dic={}
    for k,v in zip(key,value):
        if k in dic:
            if v not in dic[k]: #Esto asegura que el valor no se repita
                dic[k].append(v)
        else:
            dic[k]=[v]
    resultado = [(k, sorted(v)) for k, v in sorted(dic.items())]
    return resultado
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
if __name__ == "__main__":
    print(pregunta_08())