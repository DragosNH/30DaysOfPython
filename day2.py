# --- Day 2: 30 Days of python programming ---

# Exercice 1
first_name = 'Dragos'
last_name = 'Enache'
full_name = first_name + " " + last_name
country = 'France'
city = 'Saint - Louis'
age = 3000
year = 2025
is_maried = False
is_true = True
is_light_on = False

full_info = {
    'firstname' : "Dragos",
    'lastname' : "Enache",
    'country' : 'France',
    'city' : 'Saint - Louis'
}

# Exercice 2
print(f"First name:  {type(first_name)}")
print(f"Last name: {type(last_name)}")
print(f"Full name {type(full_name)}")
print(f"Country:  {type(country)}")
print(f"City {type(city)}")
print(f"Age:  {type(age)}")
print(f"Year: {type(year)}")
print(f"Is maried:  {type(is_maried)}")
print(f"Is true:  {type(is_true)}")
print(f"Light on:  {type(is_light_on)}")
print(f"Full info:  {type(full_info)}")

print("----------------")

print(f"Lenght of first_name : {len(first_name)}")
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
add_num = num_one + num_two
substract_num = num_one - num_two
multiply_num = num_one * num_two
divide_num = num_one / num_two
modulo_num = num_two % num_one
power_num_one = num_one ** num_two
floor_division = num_one // num_two

import math

area_of_circle = math.pi * 30**2
circum_of_circle = 2 * math.pi * 30

print(f"Area of circle with a radius of 30: {area_of_circle}")
print(f"Area of circumference with a radius of 30: {circum_of_circle}")

radius = int(input('Insert radius value: '))

area_of_circle = math.pi * radius**2
print(f"The area is: {area_of_circle}")

first_name = str(input('Insert your first name: '))
last_name = str(input('Insert your last name: '))
country = str(input('Insert your country name: '))
age = int(input('Insert your age: '))

print(help('keywords'))