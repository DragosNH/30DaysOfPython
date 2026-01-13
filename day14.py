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

# 5. Use for loop to print each name in the names list.

def show_names_list(names):
    for i in names:
        print(i)

# show_names_list(names)

# 6. Use for loop to print each number in the numbers list.
def print_each_number(num=numbers):
    for i in num:
        print(i)

# print_each_number()

# --- Level 2 ---
# 1. Use map to create a new list by changing each country to uppercase in the countries list. 
def uppercase_countries(country):
    return country.upper()

upper_countries = map(uppercase_countries, countries)

# print(list(upper_countries))

# 2. Use map to create a new list by changing each number to its square in the numbers list
def square_numbers(num):
    return num ** 2

suqared_numbers = map(square_numbers, numbers)

# print(list(suqared_numbers))

# 3. Use map to change each name to uppercase in the names list

def screamed_names(name):
    return name.upper()

I_scream_your_names = map(screamed_names, names)

# print(list(I_scream_your_names))

# 4. Use filter to filter out countries containing 'land'.

def filter_countries(coutry):
    if "land" in coutry:
        return False
    return True

non_land_countries = list(filter(filter_countries, countries))

# for x in non_land_countries:
#     print(x)

# 5. Use filter to filter out countries having exactly six characters.
def long_countries(str):
    if len(str) == 6:
        return False
    return True

short_countries = list(filter(long_countries, countries))
# print(short_countries)

# 6. Use filter to filter out countries containing six letters and more in the country list.
def too_long_names(str):
    if len(str) >= 6:
        return False
    return True

more_than_six = (list(filter(too_long_names, countries)))

# print(more_than_six)

# 7. Use filter to filter out countries starting with an 'E'
def remove_e(str):
    if "e" in str or "E" in str:
        return False
    return True

countries_without_e = list(filter(remove_e, countries))
# print(countries_without_e)

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
uppercase_countries_without_e = list(filter(remove_e, list(map(uppercase_countries, countries))))
# print(uppercase_countries_without_e)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(string):
    return list(filter(lambda item: type(item) is str, string))

random_list = ["Yes", 29, "No"]

# print(get_string_lists(random_list))

# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce 

def sum_of_numbers(x, y):
    return int(x) + int(y)

total = reduce(sum_of_numbers, numbers)

print(total)
