# Autores: Gerardo André Fernández Cruz, Leonardo Dufrey Mejía Mejía, Abby Sofia Donis Agreda
# Fecha de creación: 2024-10-06
# Fecha de actualización: 2024-10-06
# Versión: 1.1
# Descripción: Función Euclidean, algoritmo euclidiano para encontrar el mcd. 

def mcd_euclidiano(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Validación input
def input_u(mensaje):
    while True:
        valor_input = input(mensaje)
        try:
            return int(valor_input)
        except ValueError:
            print("Ingrese solamente numeros, intente de nuevo")

# Solicitar entrada al usuario
a = input_u("Ingrese un entero positivo a: ")
b = input_u("Ingrese un entero positivo b: ")

# Calcular el MCD
resultado = mcd_euclidiano(a, b)

# Mostrar el resultado
print(f"El mcd de {a} y {b} es {resultado}.")
