
#init
from random import randint
import sys
import textwrap
import nltk
import re
import string
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

file_name = 'final.txt'
with open(file_name, 'r', encoding="utf8") as f:
    text_data = f.read().lower()
    words = re.findall(r'\w+', text_data)

vocab = set(words)


text = []
word_list = []
i = 0
n = 0
wrapper = textwrap.TextWrapper(width=100)
word_count = 0
letters = []
score = 0
current = 0
c = 0.1
next = ""
target = ""
with open('fantisy.txt','r') as file:
    sample = file.read()

#functions


#code
sample = sample.split(" ")
sample = list(sample)

word_count = input("word count: ")
word_count = int(word_count)

text.append(input("starting word: "))

while i < word_count:

    target = text[i]
    n = 0
    letters = []

    for item in sample:
        if sample[n] == target and n + 1 < len(sample):
            letters.append(sample[n + 1])
        n += 1

    score = 0
    n = 0

    for item in letters:
        current = letters.count(letters[n])
        current += score * (randint(1,10) / 10)
        if current > score:
            score = current
            next = letters[n]
        n += 1

    text.append(next)

    i += 1

text = str(text)

text = text.replace("[","")
text = text.replace("]","")
text = text.replace(",","")
text = text.replace("'","")

text = text.replace("@",'"')
text = text.replace("^","'")

text = (text+".")

word_list = wrapper.wrap(text=text)

for element in word_list:
    print(element)

