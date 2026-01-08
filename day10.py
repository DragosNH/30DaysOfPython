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

for i in range(1, 100, 2):
    print(i)
