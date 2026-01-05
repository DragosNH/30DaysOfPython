# --- Day 7: 30 Days of python programming ---
# --- Level 1 ---
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
# print(len(it_companies)) #7

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Cyber-Duck', 'Ubisoft', 'EA Games'])

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')

# 5.What is the difference between remove and discard
"""
remove() reises a KeyError if the element is not found while discard() does not rise an error.
"""