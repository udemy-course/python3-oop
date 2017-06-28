

d = {
    'Name': 'Jood',
    'Age': 9,
    'Grade': 5,
}


print("dict['Age'] =", d['Name'])
print("dict['Age'] =", d['Age'])


print(d.keys())

print(d.values())

print(d.get('Name'))

del d['Name']
print(d)

d.clear()
print(d)
