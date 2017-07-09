

"""
The def header line specifies a function name that is assigned the function object,
along with a list of zero or more arguments (sometimes called parameters) in parentheses.
The argument names in the header are assigned to the objects passed in parentheses at the point of call.


Function bodies often contain a return statement:

def <name>(arg1, arg2,... argN): ...
    return <value>
"""


# Definition
def sum(a, b):
    c = a + b
    print(c)


# calls
d = sum([1,2], [3, 4])
