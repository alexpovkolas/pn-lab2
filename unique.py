from collections import Counter


def compress(seq):
    result = Counter()
    for item in seq:
        result[item] += 1
    return result.items()
