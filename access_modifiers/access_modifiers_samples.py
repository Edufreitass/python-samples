# https://pynative.com/python-encapsulation/#h-private-member
class Student:
    __schoolName = 'XYZ School'  # private class attribute

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
        self.__salary = age  # private instance attribute

    def public_method(self):
        print('This is public method.')

    def _protected_method(self):
        print('This is protected method.')

    def __display(self):  # private method
        print('This is private method.')


if __name__ == '__main__':
    std = Student("Bill", 25)
    print(std.__schoolName)  # AttributeError
    print(std.__name)  # AttributeError
    print(std.__display())  # AttributeError

    # std.public_method()
    # std._protected_method()
    # std.__display()  # AttributeError