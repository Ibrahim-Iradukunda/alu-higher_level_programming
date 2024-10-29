#!/usr/bin/python3
safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, 5)  # since we can't use len(), using the exact number
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, 7)  # more than length of the list
print("nb_print: {:d}".format(nb_print))
