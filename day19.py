# --- Day 19: 30 Days of python programming ---
# --- Level 1 ---

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
"""
I. Read obama_speech.txt file and count number of lines and words
II. Read michelle_obama_speech.txt file and count number of lines and words
III. Read donald_speech.txt file and count number of lines and words
IV. Read melina_trump_speech.txt file and count number of lines and words
"""

def lines_count(filename):
    line_count = 0
    word_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")

# lines_count('files/obama_speech.txt')
# lines_count('files/michelle_obama_speech.txt')
# lines_count('files/donald_speech.txt')
# lines_count('files/melina_trump_speech.txt')

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

def most_spoken_languages(fname, limit):
    # Read the josn file first
    with open(fname,'r', encoding="utf8") as f:
        data = f.read()

    # convert the data to dictionary
    
    country_data = json.loads(data)
    
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
    most_spoken =sorted_by_frq[:limit]
    return most_spoken


# print(most_spoken_languages('files/countries_data.json',10))

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(fname, limit):
    # Read the josn file first
    with open(fname,'r', encoding="utf8") as f:
        data = f.read()

    # convert the data to dictionary
    
    country_data = json.loads(data)

    country_population = {}
    for country in country_data:
       if("population" in country):
         country_population[country["name"]] = country["population"]
          
    return(sorted(country_population.items(), key = lambda x:x[1], reverse=True)[:limit])


# print(most_populated_countries('files/countries_data.json', 10))