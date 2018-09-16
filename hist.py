def distribute(sample, k):
    min_value = min(sample)
    max_value = max(sample)
    step = (max_value - min_value) / k
    result = [0] * k
    for item in sample:
        index = k-1 if item == max_value else int((item - min_value) // step)
        result[index] += 1

    return result


