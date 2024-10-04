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

n = int(input("Ingrese un entero positivo n: "))

es_primo, divisor = is_prime(n)

if es_primo:
    print(f"El número {n} es primo.")
else:
    print(f"El número {n} no es primo, pues lo divide {divisor}.")