# --- Day 10: 30 Days of python programming ---
# --- Level 1 ---

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
"""
for number in range(10):
    print(number)
else:
    number = number + 1
    print(number)
"""

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
"""
numbers = [10,9,8,7,6,5,4,3,2,1,0]
for number in numbers:
    print(number)
"""

"""
number = 11
while number != 0:
    number = number - 1
    print(number)
"""

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""
  #
  ##
  ###
  ####
  #####
  ######
  #######
"""

"""
symbol = '#'
triangle_height = 7
for i in range(1, triangle_height):
    print(symbol * i)
"""

# 4. Use nested loops to create the following:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

"""
symbol = "# "
symbol_width = 8
symbol_height = 8

for i in range(8, symbol_height + 1):
    for j in range(1, symbol_width + 1):
        print(symbol * i)
"""

# 5. Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

"""
for number in range(11):
    print(f"{number} x {number} = {number * number}")
"""

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
"""
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(1, len(list)):
    print(list[i])
"""

# 7. Use for loop to iterate from 0 to 100 and print only even numbers.
"""
for i in range(1, 100, 15):
    print(i)
"""

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers.
"""
for i in range(1, 100, 2):
    print(i)
"""

# --- Level 2 ---

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.

"""
max_number = 100

for i in range(max_number):
    total = sum(range(i, max_number + 1))
    print(f"The sum of all numbers is {total}")
    break
"""

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
"""
max_number = 100

for i in range(max_number):
    total_odds = sum(range(i, max_number + 1, 2))
    for j in range(max_number):
        total_evens = sum([num for num in range(1, 101) if num % 2 == 0])
        print(f"The sum of all evens is {total_odds}. And the sum of all odds is {total_evens - 50}.")
        break
    break
"""

# --- Level 3 ---
# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
"""
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

for i in countries:
    if "land" in i:
        print(i)
"""

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
"""
fruit_list = ['banana', 'orange', 'mango', 'lemon']
for i in fruit_list[::-1]:
    print(i)
"""

# --- Level 3 ---
# i. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from country_data import country_data

"""
language_count =0 
for country in country_data:
    if("languages" in country):
        language_count += len(country["languages"])

print("Total lnagauges : ", language_count) 
"""

# ii. Find the ten most spoken languages from the data
"""
languages = []
for country in country_data:
    if("languages" in country):
        for lang in country["languages"]:
            languages.append(lang)

# Create a set from list of all langauges used, that will give us unique langauges       
unique_languages = set()
unique_languages = languages

# Create a dictionary with frequency of each langauge
lang_frequency = {}
for lang in unique_languages:
    lang_frequency[lang] = languages.count(lang)

# Now sort the dictionary on frequency (descending), which will give us a list of keys
sorted_by_frq= sorted(lang_frequency.items(), key = lambda x: x[1], reverse=True)

# Now slice the first 10 from the sorted list
ten_most_spoken =sorted_by_frq[:10]

print(ten_most_spoken)
"""

# iii. Find the 10 most populated countries in the world
country_population = {}
for country in country_data:
   
    if("population" in country):
       country_population[country["name"]] = country["population"]
     
print(sorted(country_population.items(), key = lambda x:x[1], reverse=True)[:10])