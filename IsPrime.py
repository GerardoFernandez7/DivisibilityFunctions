# Autores: Gerardo André Fernández Cruz, Leonardo Dufrey Mejía Mejía, Abby Sofia Donis Agreda
# Fecha de creación: 2024-10-06
# Fecha de actualización: 2024-10-06
# Versión: 1.1
# Descripción: Función isPrime, test de primalidad utilizando la criba de Eratóstenes, 
#              determinando si un entero positivo n es primo o no. 

def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n + 1):
        if i not in not_prime:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                not_prime.add(j)
    return primes

def is_prime(n):
    if n < 2:
        return False, None
    prime_list = criba(int(n**0.5) + 1)
    for i in prime_list:
        if n % i == 0:
            return False, i
    return True, None

#Validación input
def input_u(mensaje):
    while True:
        valor_input = input(mensaje)
        try:
            return int(valor_input)
        except ValueError:
            print("Ingrese solamente numeros, intente de nuevo")

n = input_u("Ingrese un entero positivo n: ")

es_primo, divisor = is_prime(n)

if es_primo:
    print(f"El número {n} es primo.")
else:
    print(f"El número {n} no es primo, pues lo divide {divisor}.")