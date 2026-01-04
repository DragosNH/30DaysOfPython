# --- Day 6: 30 Days of python programming ---
# --- Level 1 ---

# 1.Create an empty tuple
tpl = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros_tuple = ("Catalin", "Miorel", "Prefi")
sis_tuple = ("Yes", "No", "Maybe")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = bros_tuple + sis_tuple

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parents = ("Mom", "Dad")

family_members = siblings + parents

# --- Level 2 ---

# 1. Unpack siblings and parents from family_members
bro1, bro2, bro3, sis1, sis2, sis3, mom, dad = family_members

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Banana", "Apple", "Orange", "Kiwi")
vegetables = ("Potato", "Carrot", "Cuncumber", "Onion")
animal_products = ("Cheese", "Eggs", "Milk", "Yogurt")

food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[6])

# 5. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
