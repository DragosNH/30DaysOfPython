# --- Day 4: 30 Days of python programming ---

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
random_items_list = ["lemon", "cookies", "bread", "chair", "remote", "dog", "bird person"]

# 3.Find the length of your list
# print(len(random_items_list))

# 4.Get the first item, the middle item and the last item of the list
"""
print(random_items_list[0])
print(random_items_list[3])
print(random_items_list[6])
"""

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Dragos", 3000, 1.75, "yes", "next to my neighbour"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
# print(it_companies)

# 8. Print the number of companies in the list
# print(len(it_companies))

# 9. Print the first, middle and last company
"""
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
"""

# 10. Print the list after modifying one of the companies
it_companies[0] = "Meta"
# print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Nvidia")
# print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, "OpenAi")
# print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

#  14. Join the it_companies with a string '#;  '
a_string = '#;  '
joined_items = str(it_companies) + a_string
# print(joined_items)

# 15. Check if a certain company exists in the it_companies list.
# print("IBM" in it_companies)