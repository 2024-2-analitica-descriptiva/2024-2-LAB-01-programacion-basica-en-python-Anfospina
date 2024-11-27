"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    x6=open('files/input/data.csv').readlines()
    x6=[z.replace('\n',"") for z in x6]
    x6=[z.split("\t") for z in x6]
    x6=[z[4].split(',') for z in x6[0:]]
    dic={}
    for sublista in x6:
        for item in sublista:
            key,value = item.split(":")
            value = int(value)
            if key in dic:
                dic[key].append(value)
            else:
                dic[key] = [value]
    resultado=sorted([(k,min(v),max(v)) for k,v in dic.items()])
    return resultado
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
if __name__ == "__main__":
    print(pregunta_06())