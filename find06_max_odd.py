def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    while len(data)>i:
        if max(data)%2==1:
            return max(data)
        data.remove(max(data))
        i += 1
print(find_max_odd([12,15,14,20,22]))