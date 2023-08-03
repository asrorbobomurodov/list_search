def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i = 0
    s = 0
    while len(data)>i:
        if data[i]==max(data):
            s += 1
        i = i+1
    return s
print(find_max_count([0, 8, 9, 9, 7, 0, 9]))