# --- Day 11: 30 Days of python programming ---
# --- Level 1 ---

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def return_sum(a, b):
    sum = a + b
    return sum
# print(return_sum(5,8))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
from math import pi

def area_of_circle(r):
    area = pi * r * r
    return area
# print(area_of_circle(8))

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
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
    F = (C * 9/5) +32
    print(F)
    return

# convert_celsius_to_fahrenheit(10)

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month in ("December", "January", "February"):
        return "Winter"
    elif month in ("Mars", "Avril", "May"):
        return "Spring"
    elif month in ("Juin", "Jully", "August"):
        return "Summer"
    elif month in ("September", "October", "November"):
        return "Autumn"
    else:
        return "you either typed wrong or introduced something else"

# print(check_season("January"))
# print(check_season("Mars"))
# print(check_season("August"))
# print(check_season("October"))
# print(check_season("Hot dog"))