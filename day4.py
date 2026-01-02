# --- Day 4: 30 Days of python programming ---

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
"""
string = "Thirty " + "Days " + "Of " + "Python"
print(string)
"""

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
"""
coding_string = ['Coding', 'For' , 'All']
result = ' '.join(coding_string)
print(result)
"""
# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# 4. Print the variable company using print().
"""
print(company)
"""
# 5. Print the length of the company string using len() method and print().
"""
print(len(company))
"""
# 6. Change all the characters to uppercase letters using upper() method.
"""
print(company.upper())
"""
# 7. Change all the characters to lowercase letters using lower() method.
"""
print(company.lower())
"""

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
"""
print(company.capitalize())
print(company.title())
print(company.swapcase())
"""

# 9. Cut(slice) out the first word of Coding For All string.
# print(company[7:])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
"""
sub_string = "Coding"
print(company.index(sub_string))
print(company.find("Coding"))
"""

# 11. Replace the word coding in the string 'Coding For All' to Python
# print(company.replace('Coding', 'Python'))
# company = company.replace('Coding', 'Python')

# 12.Change Python for Everyone to Python for All using the replace method or other methods.
# company = company.replace('All', 'Everyone') # There is an error in the exercice since the string never contained "Everyone" it was "All" from the begining.
# print(company)

# 13. Split the string 'Coding For All' using space as the separator (split()).
# company = company.split()

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(companies.split(","))

# 15. What is the character at index 0 in the string Coding For All.
# print(company[0])

# 16. What is the last index of the string Coding For All.
# print(company[-1])

# 17. What character is at index 10 in "Coding For All" string.
# print(company[10]) # Space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'
"""
company = "Python For Everyone"
a,b,c = company[0], company[7],company[11]
print(a)
print(b)
print(c)
"""
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
"""
company = "Coding For All"
a,b,c = company[0], company[7],company[11]
print(a)
print(b)
print(c)
"""

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# print(company.index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# print(company.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# print(company.rfind("l")) # 13

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

long_sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(long_sentence.index("because")) # 31

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# print(long_sentence.rindex("because")) # 47

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# print(long_sentence[31:55]) 

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# print(company.find("because"))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# print(long_sentence[31:55]) 

# 28. Does ''Coding For All' start with a substring Coding?
sub_string = "Coding"
# print(company.index(sub_string)) # True

# 29. Does 'Coding For All' end with a substring coding?
# print(company.index(sub_string)) # False

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_company = '   Coding For All      '
# print(new_company.strip())

# 31. Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython thirty_days_of_python
# Not clear enough

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_pythin_libraries = ' '.join(python_libraries)

# print(joined_pythin_libraries)

# 33. Use the new line escape sequence to separate the following sentences
# print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines 
"""
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""
# print('Name\tAge\tCountry\tCity\nDragos\t250\tFrance\tParis')

# 35. Use the string formatting method to display the following:
"""
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2
print(f"""
radius = {radius}\n
area = 3.14 * radius ** 2\n
The area of a circle with radius {radius} is {area} meters square.
""")

# 36. Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

print("""
8 + 6 = 14\n
8 - 6 = 2\n
8 * 6 = 48\n
8 / 6 = 1.33\n
8 % 6 = 2\n
8 // 6 = 1\n
8 ** 6 = 262144
""")