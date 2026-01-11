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

# --- Level 2 ---

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors():
    random_number = randint(0, 16777215)
    hex_number = '#' + hex(random_number)[2:]
    return hex_number

print(list_of_hexa_colors())

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colors_list = []
    colors_list.append(r)
    colors_list.append(g)
    colors_list.append(b)

    return colors_list

# print(list_of_rgb_colors())

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(type, value):
    # hex values
    random_number = randint(0, 16777215)
    hex_number = '#' + hex(random_number)[2:]
    # RGB values
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    if type == 'hexa':
        hex_list= []
        for i in range(1, value + 1):
            hex_list.append(hex_number)
            return hex_list * value

    if type == 'rgb':
        rgb_list = []
        for i in range(1, value + 1):
            # rgb_list.append(r)
            # rgb_list.append(g)
            # rgb_list.append(b)
            return [f'rgb{r,g,b}'] * value


# print(generate_colors('hexa', 3))
# print(generate_colors('rgb', 3))