def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        elif i % 7 == 0 or has_seven(i): # 这里的elif和else选择也有说法，优先elif条件好表示的，剩下的不好表示的都扔给else即可
                return f(i + 1, who - direction, -direction) # 这里非常巧妙，将clockwise和counter-clockwise两个方向量化为1和-1，
        else:
            return f(i + 1, who + direction, direction) #进而可以在确定下一个人员的时候，直接使用direction来进行加减，自身就带有方向的信息
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)