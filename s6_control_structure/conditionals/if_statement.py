
# In Python, True and False are Boolean objects of class 'bool' and they are immutable.
# Python assumes any non-zero and non-null values as True, otherwise it is False value.
# Python does not provide switch or case statements as in other languages.


# if statement

x = int(input('please enter an integer: '))
if x < 0:
    print('negative number')

# if..else statement

y = int(input('please enter an integer: '))
if y < 0:
    print('negative number')
else:
    print('positive number')

# if...elif...else statement

y = int(input('please enter an integer: '))
if y < 0:
    print('negative number')
if y > 0:
    print('positive number')
else:
    print('zero')
