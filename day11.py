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
    
# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(list, item):
    """ Function that adds an item to the list """
    list.append(item)
    return list

# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list, item):
    """ function that removes an item from a list """
    list.remove(item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(numbers):
    """ sum of all numbers """
    total = sum({i for i in range(1, numbers + 1)})
    return total

# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(odd):
    total = sum({i for i in range(2, odd + 1)})
    return total

# print(sum_of_odds(12))

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(end):
    total = 0
    for num in range(1, end + 1):
        if num % 2 == 0:
            total += num
    return total

# print(sum_of_even(20))

# --- Level 2 ---
# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(0, num+1):
        if(i%2 ==0):
            even_count+=1
        else:
            odd_count+=1
    print("The number of odds are ", odd_count)
    print("The number of evens are ", even_count)

# evens_and_odds(100)

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
        print(result)

# factorial(5)

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(param):
    if param == " " or param =="":
        print("The string is empty")
    else:
        print("The string is NOT empty")

# is_empty('')

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(mean):
    mean = sum(nums) / len(nums)

    return mean    

numbers = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
# print(calculate_mean(numbers)) 

def calculate_median(median):
    n = len(median)
    idx = n // 2

    if(n % 2 != 0 ): 
        return sorted(median)[idx]
    return sum(sorted(median)[idx - 1:idx + 1]) / 2

print(calculate_median(numbers)) 
