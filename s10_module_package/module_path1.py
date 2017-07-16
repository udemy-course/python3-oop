import sys

print(sys.path)

sys.path.append('/Users/penxiao/PycharmProjects/github/udemy/python3-oop')

from s10_module_package.abc import sum


print(sum(1, 2, 3))
