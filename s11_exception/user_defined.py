# user defined exception

"""
                              Exceptions
                                  |
             --------------------------------------------
             |                                          |
     Build-in Exceptions                      User defined Exceptions

"""

#
# >>> class CustomError(Exception):
# ...     pass
# ...
#
# >>> raise CustomError
# Traceback (most recent call last):
# ...
# __main__.CustomError
#
# >>> raise CustomError("An error occurred")
# Traceback (most recent call last):
# ...
# __main__.CustomError: An error occurred


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!\n")
    except ValueTooLargeError:
        print("This value is too large, try again!\n")

print("Congratulations! You guessed it correctly.")
