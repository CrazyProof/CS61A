def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    # 让我想到了数学归纳法的变式，不过本题比较简单，不多赘述
    if n == 1 or n == 2:
        return n
    else:
        return n * skip_factorial(n - 2)