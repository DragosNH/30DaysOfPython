from secrets import token_hex
from random import randint

# --- Day 12: 30 Days of python programming ---
# --- Level 1 ---

# 1. Write a function which generates a six digit/character random_user_id.
def random_user_id():
    return token_hex(3)

# print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user(value):
    value = int(input("How long do you want your id to be: "))
    return token_hex(value)

# print(user_id_gen_by_user(5))

# 3.Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f'rgb{r,g,b}'

# print(rgb_color_gen())

