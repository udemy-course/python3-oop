
def func_demo(a, b):
    """ doc test demo

    >>> func_demo(1, 2)
    1
    >>> func_demo('a', 3)
    'aaa'
    >>> func_demo(3, [1])
    [1, 1, 1]
    >>> func_demo('a', [1])
    Traceback (most recent call last):
        ...
    ValueError
    """

    try:
        return a ** b
    except:
        raise ValueError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
