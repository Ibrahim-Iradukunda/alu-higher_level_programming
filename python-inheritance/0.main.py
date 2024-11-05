#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    """Example class with no attributes."""
    pass

class MyClass2(object):
    """Example class with an attribute and method."""
    my_attr1 = 3
    
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
