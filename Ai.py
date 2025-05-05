
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
end = False
score = 0
current = 0
c = 0.1
next = ""
target = ""

with open('fantisy.txt','r') as file:
    sample = file.read()

#functions

def count_word_frequency(words):
    word_count2 = {}
    for word in words:
        word_count2[word] = word_count2.get(word, 0) + 1
    return word_count2

word_count2 = count_word_frequency(words)

def calculate_probability(word_count2):
    total_words = sum(word_count2.values())
    return {word: count / total_words for word, count in word_count2.items()}

probabilities = calculate_probability(word_count2)

lemmatizer = WordNetLemmatizer()

def lemmatize_word(word):
    """Lemmatize a given word using NLTK WordNet Lemmatizer."""
    return lemmatizer.lemmatize(word)

def delete_letter(word):
    return [word[:i] + word[i+1:] for i in range(len(word))]

def swap_letters(word):
    return [word[:i] + word[i+1] + word[i] + word[i+2:] for i in range(len(word)-1)]

def replace_letter(word):
    letters2 = string.ascii_lowercase
    return [word[:i] + l + word[i+1:] for i in range(len(word)) for l in letters2]

def insert_letter(word):
    letters2 = string.ascii_lowercase
    return [word[:i] + l + word[i:] for i in range(len(word)+1) for l in letters2]

def generate_candidates(word):
    candidates = set()
    candidates.update(delete_letter(word))
    candidates.update(swap_letters(word))
    candidates.update(replace_letter(word))
    candidates.update(insert_letter(word))
    return candidates

def generate_candidates_level2(word):
    level1 = generate_candidates(word)
    level2 = set()
    for w in level1:
        level2.update(generate_candidates(w))
    return level2

def get_best_correction(word, probs, vocab, max_suggestions=5):
    candidates = (
        [word] if word in vocab else list(generate_candidates(word).intersection(vocab)) or 
        list(generate_candidates_level2(word).intersection(vocab))
    )
    return sorted([(w, probs.get(w, 0)) for w in candidates], key=lambda x: x[1], reverse=True)[:max_suggestions]

#code
sample = sample.split(" ")
sample = list(sample)
print("\n type STOP to quit")
print("\n")
while not end:

    text = []
    i = 0
    n = 0
    letters = []
    score = 0
    current = 0
    next = ""
    target = ""

    word_count = input("word count: ")
    word_count = int(word_count)

    user_input = input("starting word: ")
    if user_input == "STOP":
        end = True

    text.append(user_input)

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
            if current > score:
                score = current
                next = letters[n]
            n += 1

        user_input = (str(next))
        suggestions = get_best_correction(user_input, probabilities, vocab, max_suggestions=5)
        next = [next]
        for suggestion in suggestions:
            next.append(suggestion[0])
            n = 0
        text.append(next[n])
        for c in sample:
            if c == next[n]:
                sample.remove(str(next[n]))
            
        print(text)
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

print("good bye")