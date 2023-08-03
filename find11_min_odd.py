def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    while True:
        if min(data)%2!=0:
            return min(data)
        data.remove(min(data))
print(find_min_odd([8, 2, 8, 5,4]))