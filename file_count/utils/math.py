def classic_mean(list):
    return sum(list) / len(list)


def mean_accumulated(new_value, accumulated_mean=0, size=0):
    variance = new_value - accumulated_mean
    return accumulated_mean + variance / (size + 1)
