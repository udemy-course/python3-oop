
# Useful functions

list1 = [1, 2, 3]
list2 = [2, 3, 4, 5, '6']

# len(list)
print('length of list2 =', len(list2))

# max(list)
print('max number in list1 =', max(list1))

# min(list)
print('Min number in list1 =', min(list1))


# common list methods
list3 = [1, 2, 3]
print('list3 =', list3)

# list.append(obj)
list3.append(4)
print('list3 =', list3)

# list.insert(index, obj)
list3.insert(1, 2)
print('list3 =', list3)

# list.count(obj)
print('list3.count 2 =', list3.count(2))

# list.index(obj)
print('index of 2 =', list3.index(2))

# list.remove(obj)
list3.remove(2)
print('list3 =', list3)


# list.reverse()
list3.reverse()
print('list3 =', list3)

# list.sort()
list3.sort()
print('list3 =', list3)
