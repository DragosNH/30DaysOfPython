# --- Day 13: 30 Days of python programming ---

# 1. Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_numbers = [i for i in numbers if i < 0]

# print(negative_numbers)

# 2. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattend_list = [ num for i in list_of_lists for num in i]

last_flatten = [flat for j in flattend_list for flat in j]

# print(last_flatten)

# 3. Using list comprehension create the following list of tuples:
"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""

new_numbers = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
# print(new_numbers)

# 4. Flatten the following list to a new list:
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [[item[0].upper(),item[0].upper()[:3],item[1].upper()]  for country in countries for item in country ]
# print(new_list)

# 5. Change the following list to a list of dictionaries:

new_country_list = [
            {'country' : item[0].upper(), 'city' : item[1].upper()}
            for country in countries
            for item in country
]

# print(new_country_list)

# 6. Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

new_names_list = ["{} {}".format(item[0], item[1]) 
            for tuples in names for item in tuples 
           ]

print(new_names_list)