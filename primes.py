from math import sqrt


def get_primes(n):
    return [x for x in range(2, n + 1) if all([x % i for i in range(2, int(sqrt(x)) + 1)])]
