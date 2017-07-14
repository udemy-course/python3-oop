
class Animal:

    def eat(self):
        print('Animal is eating...')


class Bird(Animal):

    def sing(self):
        print('Bird is singing..')

    def eat(self):
        print('Bird is eating')


class Dog(Animal):

    def run(self):
        print('Dog is running')

    def eat(self):
        print('Dog is eating')

a = Animal()
a.eat()


b = Bird()
b.eat()
b.sing()

d = Dog()
d.eat()
d.run()
