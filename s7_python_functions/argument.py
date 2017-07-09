
# required argument, the arguments passed to the function in correct positional order. 


def func(a, **b):
    print(b)
    print(b['d'])



func(a=1, b=2, c=3, d=4)

# Variable-length arguments: This used when you need to process unspecified additional arguments.
# An asterisk (*) is placed before the variable name in the function declaration.
