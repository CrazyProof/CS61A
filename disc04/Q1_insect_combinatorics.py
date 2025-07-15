def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 and n == 1:
        return 1
    if m <= 0 or n <= 0:
        return 0
    else:
        return paths(m - 1, n) + paths(m, n - 1)