""" This is a docstring for the module dstring. """


def func1():
    """ This is a docstring for the function func1. """
    pass


def func2():
    """ This is a docstring for the function func2. """
    pass


class MyClass:
    """ This is a docstring for the class MyClass. """

    def method1(self):
        """ This is a docstring for the method method1. """
        pass

    def method2(self):
        """ This is a docstring for the method method2. """
        pass


print(func1.__doc__)
print(func2.__doc__)
print(MyClass.__doc__)
print(MyClass.method1.__doc__)
print(MyClass.method2.__doc__)

print(func1())
