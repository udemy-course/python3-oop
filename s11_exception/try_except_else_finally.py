
def divide(x, y):
    try:
        result = x / y
        a = [1]
        print(a[0])
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print('type error')
    except Exception:
        print('base exception')
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(1, 2)