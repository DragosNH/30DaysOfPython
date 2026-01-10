"""Module providing a function printing python version."""
from math import pi

# --- Day 11: 30 Days of python programming ---
# --- Level 1 ---

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def return_sum(a, b):
    """Function that sums two numbers."""
    sum = a + b
    return sum
# print(return_sum(5,8))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    """Function that calculates the area of a circle."""
    area = pi * r * r
    return area
# print(area_of_circle(8))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    """Function that adds all nums."""
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return 'At least one argument is Nan'
    
    for num in nums:
        total += num
    return total
# print(add_all_nums(5, 8, -5, '1', 154)) # Is working

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(C):
    """Function that converts °C to °F."""
    F = (C * 9/5) +32
    print(F)
    return

# convert_celsius_to_fahrenheit(10)

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    """Function that returns the season depending on the month."""
    if month in ("December", "January", "February"):
        return "Winter"
    elif month in ("Mars", "Avril", "May"):
        return "Spring"
    elif month in ("Juin", "Jully", "August"):
        return "Summer"
    elif month in ("September", "October", "November"):
        return "Autumn"
    else:
        return "You either typed wrong or introduced something else"

# print(check_season("January"))
# print(check_season("Mars"))
# print(check_season("August"))
# print(check_season("October"))
# print(check_season("Hot dog"))

# 6. Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    """Function printingslope."""
    return (y2 - y1) / (x2 - x1)

# print(calculate_slope(5,6,8,2))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b,c,x):
    """Function which calculates solution set of a quadratic equation."""
    equation_result = a*x**2 + b*x + c
    print(equation_result)
    return

# solve_quadratic_eqn(5,8,2,6)

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(*args):
    """Function that returns a list. """
    for i in args:
        print(i)
    return 

# print_list('yes', 'no', 'maybe', 'of course')

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    list = []
    if len(lst) > 0:
        for i in range(len(lst) -1, -1, -1):
            list.append(lst[i])
        return list 

nums = [1,2,3,4,5]
letters = ["A", "B", "C"]

# print(reverse_list(nums))
# print(reverse_list(letters))

# 10.Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items.

def capitalize_list_items(lst):
    list = [word.capitalize() for word in lst]
    return list

random_list = ["this", "is", "a", "list"]

# print(capitalize_list_items(random_list))
    