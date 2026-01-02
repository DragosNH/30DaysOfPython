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
sub_string = "Coding"
print(company.index(sub_string))
print(company.find("Coding"))