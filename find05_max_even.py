def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    while len(data)>i:
        if max(data)%2==0:
            return max(data)
        data.remove(max(data))
        i += 1
print(find_max_even([0,7,9,5,4]))
