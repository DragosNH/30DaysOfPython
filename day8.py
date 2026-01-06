# --- Day 8: 30 Days of python programming ---

# 1. Create an empty dictionary called dog
dog = dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "Sparky"
dog['color'] = "grey"
dog['breed'] = "beagle"
dog['legs'] = 4
dog['age'] = 3

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name" : "John",
    "last_nale" : "Collone",
    "gender" : "male",
    "age" : 21,
    "married" : False,
    "skills" : ["sleeping", "eating", "drinking", "walking"],
    "country" : "United Kingdom",
    "city" : "London",
    "adress" : "2nd house on the left",
}

# 4. Get the length of the student dictionary
# print(len(student)) #9

# 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))