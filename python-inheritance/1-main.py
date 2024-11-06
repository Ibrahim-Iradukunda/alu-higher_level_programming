#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

# Test case: class creation, multiple appends, regular print and sorted print
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

# Test case: class creation, regular print and sorted print
my_list = MyList()
print(my_list)
my_list.print_sorted()

# Test case: class creation, multiple appends (negative number), regular print and sorted print
my_list = MyList()
my_list.append(-1)
my_list.append(3)
my_list.append(0)
my_list.append(2)
my_list.append(-5)
print(my_list)
my_list.print_sorted()
print(my_list)
