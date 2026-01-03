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
# print(it_companies)

#  14. Join the it_companies with a string '#;  '
a_string = '#;  '
joined_items = str(it_companies) + a_string
# print(joined_items)

# 15. Check if a certain company exists in the it_companies list.
# print("IBM" in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
# print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
# print(it_companies)

# 18. Slice out the first 3 companies from the list
# print(it_companies[3:])

# 19. Slice out the last 3 companies from the list
# print(it_companies[:-3])

# 20. Slice out the middle IT company or companies from the list
# print(it_companies[:4] + it_companies[4 + 1:])

# 21. Remove the first IT company from the list
# it_companies.pop(0)
# print(it_companies)

# 22. Remove the middle IT company or companies from the list
# print(len(it_companies)//2) #Middle index is 4
# it_companies.pop(4)
# print(it_companies)

# 23. Remove the last IT company from the list
# it_companies.pop()
# print(it_companies)

# 24. Remove all IT companies from the list
# it_companies.clear()
# print(it_companies)

# 25. Destroy the IT companies list
del it_companies