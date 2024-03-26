import nltk
from nltk.stem import WordNetLemmatizer

file = open('C:\\work\\2 semestr\\ЕЯИ\\test.txt', 'r')
token_file = open('tokens.txt', 'r+')
lemmatizer = WordNetLemmatizer()
stemmed_words_file = open('leksemes.txt', 'w')
for line in token_file:
    for word in line.split():
        stemmed_words_file.write(lemmatizer.lemmatize(word) + ' ')