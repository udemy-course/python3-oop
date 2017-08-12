

def add(a, b):
    """
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("a/b must be exact integer")

if __name__ == '__main__':
    x = 1
    y = 2
    print(x, '+', y, '=', add(x, y))
