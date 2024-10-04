def mcd_euclidiano(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicitar entrada al usuario
a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))

# Calcular el MCD
resultado = mcd_euclidiano(a, b)

# Mostrar el resultado
print(f"El mcd de {a} y {b} es {resultado}.")
