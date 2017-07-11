
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10
print(my_list)

f = open("output.txt", "a")

for item in my_list:
    f.write(str(item) + "\n")

print(f.closed)

f.close()


with open('test.txt', 'w') as f1:
    f1.write('test\n')
    f1.write('test\n')

print(f1.closed)