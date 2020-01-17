import time as t


def primes_method0(n):
    primes = [2, 3, 5, 7]
    if n <= 7:
        return primes
    for num in range(3, n, 2):
        if all(num % x != 0 for x in primes):
            primes.append(num)
    return primes


def primes_method1(n):
    out = list()
    for num in range(1, n + 1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return out


def primes_method2(n):
    out = list()
    for num in range(1, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            out.append(num)
    return out


def primes_method3(n):
    out = list()
    for num in range(1, n + 1):
        if all(num % i != 0 for i in range(2, int(num**.5) + 1)):
            out.append(num)
    return out


def primes_method4(n):
    out = list()
    out.append(2)
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(num**.5) + 1)):
            out.append(num)
    return out


def primes_method5(n):
    out = list()
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


# start = t.perf_counter()
# print(primes_method1(100000))
# print(t.perf_counter() - start)

start = t.perf_counter()
print(primes_method5(100000))
print(t.perf_counter() - start)
