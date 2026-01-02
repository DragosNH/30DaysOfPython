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

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

a,b,c = company[0], company[7],company[11]
print(a)
print(b)
print(c)

