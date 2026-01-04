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