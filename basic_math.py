
def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list) / len(number_list)
    return mean


def get_median(number_list):
    length = len(number_list)
    number_list.sort()
    if length % 2:
        median = number_list[length // 2]
    else:
        median = (number_list[length // 2] + number_list[length // 2 - 1]) / 2
    return median
