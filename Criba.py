def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n):
        if i not in not_prime:
            primes.append(i)
            for j in range(i*i, n, i):
                not_prime.add(j)
    return primes

# Solicitar entrada al usuario
a = int(input("Ingrese un numero: "))

# Mostrar el resultado
print(criba(a))