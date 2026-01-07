# --- Day 9: 30 Days of python programming ---
#  --- Level 1 ---

# 1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""
"""
age = int(input("Enter your age: "))

if age > 18:
    print("You are old enough to learn to drive.")
else:
    print(f'You need {18 - age} more years to learn to drive.')
"""

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
"""
Enter your age: 30
You are 5 years older than me.
"""

"""
my_age = 25
your_age = int(input('Enter your age: '))

if my_age < your_age:
    if your_age == my_age + 1:
        print("You are one year older than me")
    else:
        print(f"You are {your_age - my_age} years older than you")
else:
    if my_age == your_age + 1:
        print("I am one year older than me")
    else:
        print(f"I am {my_age - your_age} years older than you")
"""

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
"""
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""

"""
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")
"""

#  --- Level 2 ---

# 1. Write a code which gives grade to students according to theirs scores:
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

""""
score = int(input("Enter your score: "))

if score >= 80 and score <= 100:
    print("A")
elif score >= 70 and score <= 79:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
elif score >= 0 and score <= 49:
    print("F")
else:
    print("Such score does not exists")
"""

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""
month = str(input("Add a month: ")).capitalize()

if month == "September" or month == "October" or month == "November":
    print("Autumn")
elif month == "December" or month == "January" or month == "February":
    print("Winter")
elif month == "March" or month == "April" or month == "May":
    print("Spring")
else: 
    print("Summer")
"""

# 3. The following list contains some fruits:
"""
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""

"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input("Add a fruit in the basket: "))

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
"""

# --- Level 3 ---
# 1. Here we have a person dictionary. Feel free to modify it!


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
"""
if person['skills']:
    print(person['skills'])
"""

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
"""
if person['skills']:
    if 'Python' in person['skills']:
        print(person['skills'])
"""

# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
"""
if 'JavaScript' and 'React' and 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'JavaScript' and 'React' in person['skills']:
    print('He is a front end developer')
else:
    print('unknown title')
"""

#  * If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] == True and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']} and he is married")