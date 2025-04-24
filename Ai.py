
#init
from random import randint

text = []
i = 0
n = 0
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

c = input("creativity: ")
c = int(c)

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
        if current + (randint(-c,c)) > score:
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
text = text.replace("\n\n\n","")

text = text.replace("@",'"')
text = text.replace("^","'")

text = (text+".")

print(text)

