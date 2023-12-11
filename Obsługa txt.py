from Funkcje import *

content = file_reading('U2.txt')
content = cleansed_text(content)
print(f'Number of words: {number_of_words(content)}')
print(f'Number of unique words: {unique_words(content)}')
print(f'Number of repetitions: {repetitions(content)}')
print(f'The most frequent words are: {repetitions(content)}')

#jeśli słowo powtarza się więcej niż 5% wszystkich słów, napisz
