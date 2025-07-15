# 这道题目比较难，参考了hint才做出来
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    # 这里需要对n==2单独判断，不然会返回False
    if n == 2:
        return True
    # 定义一个内部函数，作用是从2开始依次尝试能否整除n，直到sqrt(n)。递归体现在i+1
    # 如果是全局函数会有问题，无法接受n作为参数 maybe
    def f(i):
        # 添加两个终结条件，因为是判断函数，所以是True和False两种情况。
        if n % i == 0:
            return False
        elif i * i > n:
            return True
        else:
            return f(i + 1)
    # 从2开始递归
    return f(2)