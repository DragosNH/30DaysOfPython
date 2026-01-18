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

        # text_read = open(f'files/{file}')
        # lines = text_read.readlines()
        # print(lines)
        # text_read.close()

lines_count('files/obama_speech.txt')
lines_count('files/michelle_obama_speech.txt')
lines_count('files/donald_speech.txt')
lines_count('files/melina_trump_speech.txt')