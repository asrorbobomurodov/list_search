def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """

    return data.index(max(data))
print(find_max_index([0, 5, 8, 9, 70, 2]))
