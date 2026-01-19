# --- Day 20: 30 Days of python programming ---
import requests

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

def find_most_common_words(fname,limit):
    f = open(fname,"r")    
    lines = f.readlines()
    words = []
    for line in lines:
        for word in line.split():
         words.append(word)    
    
    unqiue_words= set()
    unqiue_words= words


    # Create a dictionary with frequency of each word
    word_frequency = {}
    for word in unqiue_words:
        word_frequency[word] = words.count(word)
        

    # Now sort the dictionary on frequency (descending), which will give us a list of keys
    sorted_by_frq= sorted(word_frequency.items(), key = lambda x: x[1], reverse=True)
    # Now slice the first 10 from the sorted list
    most_common_words =sorted_by_frq[:limit]
    return most_common_words

# print(find_most_common_words("files/romeo_and_juliet.txt", 10)) #[('the', 762), ('I', 549), ('and', 539), ('to', 522), ('of', 485), ('a', 453), ('in', 330), ('is', 322), ('my', 310), ('with', 274)]

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
"""
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats
"""

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
print(cats_api)