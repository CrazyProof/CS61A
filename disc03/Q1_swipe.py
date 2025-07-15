def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    # 刚开始使用return swipe(not_last)进行递归，想了很久都不对
    # 递归不一定需要使用return语句来进行递归，函数体中间调用自身也是递归
    if n < 10:
        print(n)
    else:
        not_last, last = n // 10, n % 10
        print(last)
        swipe(not_last)
        print(last)

