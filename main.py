import re

# Open the file and read its content
with open("positive-words.txt", 'r', encoding='ISO-8859-1') as filep:
    positive_words = [line.strip() for line in filep if line.strip()]  # Create a list of words

with open("positive-words.txt", 'r', encoding='ISO-8859-1') as filen:
    negative_words = [line.strip() for line in filen if line.strip()]  

# Get the comment input
comment = input("Enter your comment: ")
positive = 0
negative = 0

# Split the comment into words
x = re.split("\s", comment)

# Count positive and negative words
for i in x:
    if i in positive_words:  # Check if the word is in the positive words list
        positive += 1
    elif i in negative_words:
        negative +=1

# Desiding that the comment is positive or negative
if positive > negative:
    print("positive")
else:
    print("negative")