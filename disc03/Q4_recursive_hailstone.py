def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)
# 由于返回序列元素个数，所以return语句后面的就在计算个数，而不是为了打印，打印功能在函数体内部实现。
def even(n):
    return hailstone(n // 2) + 1

def odd(n):
    # 整个递归一定要有终止条件，即base case
    if n == 1:
        return 1
    return hailstone(3 * n + 1) + 1