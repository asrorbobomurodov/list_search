def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    return data.index(min(data))
print(find_min_index([-9,-87,-87,21,0]))

