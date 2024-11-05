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

# Correct output - case: int
print(lookup(int))

# Correct output - case: float
print(lookup(float))

# Correct output - case: object
print(lookup(object))

# Correct output - case: list
print(lookup(list))

# Correct output - case: class with dir method
class MyClass3():
    def dir(self):
        return ["my_class", "is", "empty"]

print(lookup(MyClass3))

# Correct output - case: class with no attributes or methods
class MyClass4():
    pass

print(lookup(MyClass4))

# Correct output - case: class with one attribute
class MyClass5():
    one_attribute = 89

print(lookup(MyClass5))

# Correct output - case: class with one method
class MyClass6():
    def one_meth(self):
        pass

print(lookup(MyClass6))
