
#Analisis de algoritmos
#Tarea 03
#Jose Alexander Artavia Quesada
#2015098028

def sumatoria_cubica(n):
    """
    Funcion que realiza el calculo de una serie
    utilizando una complejidad temporal O(n**3)

    Entrada: un numero >= 0
    Salida: resultado de la serie
    Restricciones: entrada tipo int
    """

    suma = 0
    

    for i in range(1, n+1):

        for j in range(1, i+1):

            for k in range(j, (i+j)+1):
                suma = suma + 1

    return suma
    raise NotImplementedError()

def sumatoria_constante(n):
    """
    Funcion que realiza el calculo de una serie
    utilizando una complejidad temporal O(1)

    Entrada: un numero >= 0
    Salida: resultado de la serie
    Restricciones: entrada tipo int
    """
    
    suma = int((n*(n+1)*(n+2))/3)
    
    return int(suma)
    raise NotImplementedError()

"""
print(sumatoria_cubica(2))
print(sumatoria_cubica(3))
print(sumatoria_cubica(4),"\n")

print(sumatoria_constante(2))
print(sumatoria_constante(3))
print(sumatoria_constante(4))
"""

