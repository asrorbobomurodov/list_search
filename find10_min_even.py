def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i = 0
    while len(data)>i:
        if min(data)%2==0:
            return(min(data))
        data.remove(min(data))
        i += 1
print(find_min_even([7, 8, 4, 3, 5]))

