# instance method and class method


class A(object):

    @classmethod
    def test(cls, y):
        pass

    # Instance method
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        self.test(x)

    # class method
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        cls.test(x)

    # static method
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
