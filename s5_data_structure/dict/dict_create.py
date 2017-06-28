
# Python's dictionaries are kind of hash table type which consist of key-value pairs of unordered elements. 

# Keys : must be immutable data types ,usually numbers or strings. 
# Values : can be any arbitrary Python object.


d = {}  # empty dict

d = {
    1: 1,
    2: 2,
    3: 3
}

# Python Dictionaries are mutable objects that can change their values.

print('d[0] =', d[0])

d[0] = '1111'

print(d)

# A dictionary is enclosed by curly braces ({ }), the items are separated by commas, and each key is separated from its value by a colon (:).

# Dictionary’s values can be assigned and accessed using square braces ([]) with a key to obtain its value. 
