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
# print(student['skills']) # ['sleeping', 'eating', 'drinking', 'walking']
# print(type(student['skills'])) #<class 'list'>

# 6. Modify the skills values by adding one or two skills
student['skills'].append('Runing away from problems')
# print(student['skills'])

# 7. Get the dictionary keys as a list
student_key_list = list(student.keys())
# print(type(student_key_list))

# 8. Get the dictionary values as a list
student_value_list = list(student.values())
# print(type(student_value_list))

# 9.Change the dictionary to a list of tuples using items() method
# student = student.items()
# print(type(student))

# 10. Delete one of the items in the dictionary
del student['married']
# print(student)

# 11. Delete one of the dictionaries
del student
print(student_key_list)