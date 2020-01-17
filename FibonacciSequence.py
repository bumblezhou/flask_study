import numpy
import time as t


def get_fibonacci_squence0(x):
    if x <= 2:
        return [0, 1]
    return [(numpy.matrix('2 1; 1 1') ** (n // 2))[0, (n + 1) % 2] for n in range(x)]


def get_fibonacci_squence1(x):
    if x <= 2:
        return [0, 1]
    return [(4 << n * (3 + n)) // ((4 << 2 * n) - (2 << n) - 1) & ((2 << n) - 1) for n in range(1, x)]


start = t.perf_counter()
print(get_fibonacci_squence0(100))
print(t.perf_counter() - start)

start = t.perf_counter()
print(get_fibonacci_squence1(100))
print(t.perf_counter() - start)
