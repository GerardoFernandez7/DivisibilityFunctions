# Autores: Gerardo André Fernández Cruz, Leonardo Dufrey Mejía Mejía, Abby Sofia Donis Agreda
# Fecha de creación: 2024-10-06
# Fecha de actualización: 2024-10-06
# Versión: 1.1
# Descripción: Función Criba, criba de Eratóstenes para encontrar números primos
#              menores o iguales a un numero positivo dado n. 

def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n):
        if i not in not_prime:
            primes.append(i)
            for j in range(i*i, n, i):
                not_prime.add(j)
    return primes

#Validación input
def input_u(mensaje):
    while True:
        valor_input = input(mensaje)
        try:
            return int(valor_input)
        except ValueError:
            print("Ingrese solamente numeros, intente de nuevo")

# Solicitar entrada al usuario
a = input_u("Ingrese un numero: ")

# Mostrar el resultado
print(criba(a))