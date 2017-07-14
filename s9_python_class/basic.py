# class definition


class MyClass:
    pass

# The __init__() Method
# attributes
# methods

class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def sayhi(self):
        print("Hi, my name is %s, and I'm %s" % (self.__name, self.__age))

    def get_age(self):
        return self.__age

    def set_age(self, num):
        if isinstance(num, int):
            if num > 0:
                self.__age = num
                return
        print('format error')


# class instance

someone = People(name='Jack', age=20)
print(someone.get_age())
someone.set_age(num='ab')
print(someone.get_age())