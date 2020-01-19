import numpy
import time as t
from functools import reduce


def get_fibonacci_sequence0(x):
    if x <= 2:
        return [0, 1]
    return [(numpy.matrix('2 1; 1 1') ** (n // 2))[0, (n + 1) % 2] for n in range(x)]


def get_fibonacci_sequence1(x):
    if x <= 2:
        return [0, 1]
    return [(4 << n * (3 + n)) // ((4 << 2 * n) - (2 << n) - 1) & ((2 << n) - 1) for n in range(1, x)]


def get_fibonacci_sequence2(x):
    if x <= 2:
        return [0, 1]
    return [(lambda n:reduce(lambda x, n:[x[1], x[0] + x[1]], range(n), [0, 1])[0])(n) for n in range(x)]


start = t.perf_counter()
print(get_fibonacci_sequence0(100))
print(t.perf_counter() - start)

start = t.perf_counter()
print(get_fibonacci_sequence1(100))
print(t.perf_counter() - start)

start = t.perf_counter()
print(get_fibonacci_sequence2(100))
print(t.perf_counter() - start)
