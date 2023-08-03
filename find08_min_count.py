def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    return data.count(min(data))
print(find_min_count([-9,-89,8,-89,-4]))
