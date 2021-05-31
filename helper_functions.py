def len_copy(word):
    """ Return the length of word.

    >>> length('name')
    4
    >>> length('')
    0
    """

    cntr = 0
    for _ in word:
        cntr += 1
    return cntr