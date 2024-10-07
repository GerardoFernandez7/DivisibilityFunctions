# Autores: Gerardo André Fernández Cruz, Leonardo Dufrey Mejía Mejía, Abby Sofia Donis Agreda
# Fecha de creación: 2024-10-06
# Fecha de actualización: 2024-10-06
# Versión: 1.1
# Descripción: Función Bezout, algoritmo matricial para encontrar los coeficientes
#              de Bézout de dos números enteros a y b. 
# Referencias: Python: Operadores aritméticos - R que R. (n.d.). https://rquer.netlify.app/python_basic/python_operations/ 

import numpy 

def Bezout(a, b): 
    # Ingresar los valores de a y b
    
    matriz1 = numpy.array([a,b])
    matriz2 = numpy.array([[1,0], [0,1]])
    

    #   1, 0, [a]
    #   0, 1, [b]


    while matriz1[1] != 0: 
       
        q = matriz1[0] // matriz1[1]
        matriz3 = numpy.array([[0,1], [1,-q]])
        
        matriz2 = numpy.dot(matriz2, matriz3)
        
        vec = numpy.dot(matriz3, matriz1)
    
    x, y = matriz2[0, 0], matriz2[0, 1]
    return matriz1[0], x, y


a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

gcd, x, y = Bezout(a, b)
print(f"Los coeficientes de Bézout para {a} y {b} son: x = {x}, y = {y}")
print(f"Verificación: {a}*{x} + {b}*{y} = {gcd}")
