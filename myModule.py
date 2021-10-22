def top_n(items, n):
    """Retun the top n items in an array, in desc order.

    Args:
        items (array): list or array-like object
        n (int): num if items to return

    Return:
    array: top n items, in desc order

    Egs:
    >>> top_n[8,3,2,7,4], 3
    [8,7,3] 
    """
    for i in range(n):  # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            # if this items is bigger than the next item...
            if items[j] > items[j_1]:
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!

    # get last two items
    top_n = items[n-1:]

    # return in descending order
    # return top_n[::-1]
