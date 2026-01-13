# --- Day 14: 30 Days of python programming ---
# --- Level 1 ---

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Explain the difference between map, filter, and reduce.
"""
Map function applies a given function to each element of an iterable and returns a new iterable containing the results.
Filter applies a given function to each element of an iterable and returns a new iterable containing the results.
Reduce function, which is part of the functools module, applies a function cumulatively to the elements of an iterable, reducing them to a single value.
"""

# 2. Explain the difference between higher order function, closure and decorator.
"""
A higher-order function in Python is a function that either takes one or more functions as arguments or returns a function as its result
A closure is a specific type of higher-order function that arises when a nested function captures and retains access to variables from its enclosing (outer) function's scope, even after the outer function has finished executing.
A decorator is a specialized form of a higher-order function that is used to modify or enhance the behavior of another function without altering its source code.
"""

# 3.Define a call function before map, filter or reduce, see examples.
def greet_function(arg):
    return f"Hello {arg}"

def person_function(f, name):
    greet_person = f(name + ", how are you?")
    return greet_person

greeting = person_function(greet_function, "Dragos")
# print(greeting)

# 4. Use for loop to print each country in the countries list.

def countries_list_function(countries_names):
    for i in countries_names:
        print(i)

# countries_list_function(countries)

# 5. Use for to print each name in the names list.

def show_names_list(names):
    for i in names:
        print(i)

show_names_list(names)