from re import finditer


def index(number, values, limit=5):
    positions = []
    for value in [values] if isinstance(values, int) else values:
        value_positions = [m.start() + 1 for m in finditer(str(value), number)]
        positions.extend(value_positions)
    return len(positions), sorted(positions)[:limit]
