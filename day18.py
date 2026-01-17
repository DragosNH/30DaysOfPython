# --- Day 17: 30 Days of python programming ---
# --- Level 1 ---

import re
from collections import Counter

# 1. What is the most frequent word in the following paragraph?

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def most_frequent_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(1)[0][0]

# print(most_frequent_word(paragraph))

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) 

numbers = [int(p) for p in points]
min_point = min(numbers)
max_point = max(numbers)
distance = max_point - min_point
# print(distance)

# --- Level 2 ---
# 1. Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(var):
    if "-" in var:
        print(False)
    elif re.match(r'^\d', var):
        print(False)
    else:
        print(True)

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True