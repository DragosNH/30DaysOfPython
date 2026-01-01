import math
# --- Day 3: 30 Days of python programming ---

# 1. 2. 3.
age = 33
height = 1.73
complex_numer = 52.68 * age **height

# 4. Calculate the base of the triangle
"""
print("Find the area of the triangle by adding the base and the hight.")
base = int(input("Enter base value: "))
height = int(input("Enter height value: "))
area = 0.5 * base * height
print(f"The area is: {area}")
"""

# 5. Calculate the parameter of the triangle
"""
print("Add the size of each angle of the trianle in order to find it's perimeter")
a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")
"""

# 6. Lenght and width of a triangle
"""
print("Calculate the perimeter of a rectangle")
length = int(input("Enter length:"))
width = int(input("Enter width:"))
area = length + width
print(f"The area is {area}")
perimeter = 2 * (length + width)
print(f"The perimeter is {perimeter}")
"""

# 7. The radius of the circle
"""
print("Enter the radius in order to find the area and the circumference")
pi = math.pi
r = int(input("Enter radius:"))
area = pi * r * r
print(f"The area is: {area}")
c = 2 * pi * r
print(f"The circumference is {c}")
"""

# 8. Calculate the slope
"""
x_intercept  = int(input("Value of x: "))
y_intercept  = 2*x_intercept - 2
print(f"y is {y_intercept}")
"""

# 9. Euclidean distance
"""
x = int(input("Value of x: "))
y = int(input("Value of y: "))
m = y*2 - y*1 / x*2 - x*1
print(f"The distance is: {m}")
"""

# 10. Comparasion
"""
print(m < y_intercept)
"""

# 11. Value of Y
"""
x = int(input("Enter the value of x: "))
y = x ^ 2 + 6 * x + 9
print(f"The value is {y}")
"""

# 12. Falsy comparison
"""
python = "python"
dragon = "dragon"
print(f"Python: {len(python)}")
print(f"Dragon: {len(dragon)}")

print(len(python) != len(dragon))
on = python and dragon

# 13. Find if both contain 'on'
print(f"Both words conain 'on'? {on.__contains__('on')}" )
"""

# 14. Find the word in sentence
"""
sentence = "I hope this course is not full of jargon."

print(sentence.__contains__("jargon"))
"""

# 16. Find the length of the text python and convert the value to float and convert it to string
"""
length_of_pyton = str(float(len("python")))
print(type(length_of_pyton))
"""

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
"""
number = int(input("Enter a vlaue: "))
if not number % 2:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
"""

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
"""
div = 7 / 3
print(div == 2.7)
"""

# 19. Check if type of '10' is equal to type of 10
"""
string = '10'
intiger = 10
print(string == intiger)
"""

# 20. Check if int('9.8') is equal to 10
"""
x = int(9.8)
print(x == 10)
"""

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
housr = int(input("Enter hours: "))
income = int(input("Enter rate per hour: "))
weekly_earning = housr * income
print(f"Your weekly earning is {weekly_earning}")
"""

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
"""
years = int(input("Enter number of years you have lived: "))
seconds_lived = (years * 365.2425) * 24 * 3600
print(f"You have lived for {seconds_lived} seconds.")
"""
# 23.

print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')