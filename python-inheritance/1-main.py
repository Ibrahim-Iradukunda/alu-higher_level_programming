#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

# Correct output - case: class creation, multiple appends, regular print and sorted print
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

# Correct output - case: class creation, regular print and sorted print
my_list = MyList()
print(my_list)
my_list.print_sorted()

# Correct output - case: class creation, multiple appends (negative number), regular print and sorted print
my_list = MyList()
my_list.append(-1)
my_list.append(3)
my_list.append(0)
my_list.append(2)
my_list.append(-5)
print(my_list)
my_list.print_sorted()
print(my_list)

# Additional tests to ensure compliance
# Test present: check instantiation
my_list = MyList()

# Test present: check inherits from list
print(isinstance(my_list, list))

# Test present: check __str__
my_list.append(10)
print(str(my_list))

# Test present: check append()
my_list.append(20)
print(my_list)

# Test present: check print_sorted() with sorted append
my_list_sorted = MyList()
my_list_sorted.append(1)
my_list_sorted.append(2)
my_list_sorted.append(3)
my_list_sorted.print_sorted()

# Test present: check print_sorted() with not sorted append
my_list_unsorted = MyList()
my_list_unsorted.append(3)
my_list_unsorted.append(1)
my_list_unsorted.append(2)
my_list_unsorted.print_sorted()

# Test present: check print_sorted() with no sorted append with negative number
my_list_mixed = MyList()
my_list_mixed.append(-3)
my_list_mixed.append(1)
my_list_mixed.append(-2)
my_list_mixed.print_sorted()

# Test present: check print_sorted() with empty list
my_list_empty = MyList()
my_list_empty.print_sorted()

# Test present: check print_sorted() returns a new list
my_list_new_list = MyList()
my_list_new_list.append(1)
my_list_new_list.append(3)
my_list_new_list.append(2)
sorted_list = my_list_new_list.print_sorted()
print(sorted_list)
