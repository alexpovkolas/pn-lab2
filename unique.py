def compress(seq):
    result = {}
    for item in seq:
        result[item] = result.setdefault(item, 0) + 1
    return result.items()
