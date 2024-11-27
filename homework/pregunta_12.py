"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    x12=open('files/input/data.csv').readlines()
    x12=[z.replace('\n',"") for z in x12]
    x12=[z.split("\t") for z in x12]
    key=[z[0] for z in x12[0:]]
    value=[z[4] for z in x12[0:]]
    suma_por_entrada=[]
    for linea in value:
        suma=0
        pares = linea.split(',')
        for par in pares:
            __, valor = par.split(':')
            suma += int(valor)
        suma_por_entrada.append(suma)
    dic={}
    for k,v in zip(key,suma_por_entrada):
        if k in dic:
            dic[k].append(v)
        else:
            dic[k]=[v]
    suma = {letra: sum(valores) for letra, valores in dic.items()}
    return dict(sorted(suma.items()))

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
if __name__ == "__main__":
    print(pregunta_12())