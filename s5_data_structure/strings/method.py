
# length of the string

x = 'abcd'
print(len(x))

# find from sting

x = 'abcd'
print('a' in x)

# Returns True if string has at least 1 character and all characters are alphanumeric and False otherwise.
# str.isalpha()

x = 'abc'
y = '123abc'

print(x.isalpha())
print(y.isalpha())

# Returns True if string contains only digits and False otherwise.
# str.isdigit()

x = 'abc123'
y = '123'

print(x.isdigit())
print(y.isdigit())

# Converts all uppercase letters in string to lowercase or uppercase
# str.lower()
# str.upper()

a = 'ABxyZ'
print(a.lower())
print(a.upper())

# Splits string according to delimiter str (space if not provided)
# and returns list of substrings.
# str.split(str=‘ ’)

x = 'this is a line'
print(x.split(' '))


# https://docs.python.org/3.4/library/stdtypes.html#string-methods