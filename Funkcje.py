def file_reading(filename):
    with open(filename, 'r', encoding='utf8') as file1:
        content = file1.read()
    return content


def number_of_words(text):
    text = text.split()
    return len(text)

def unique_words(text):
    text = text.split()
    text = set(text)
    print(text)
    return len(text)


def cleansed_text(text):
    special_characters = set('.,:(\'\"){}[]!-')
    text = text.lower()
    for char in special_characters:
        text.replace(char,'')
    return text


def repetitions(text):
    text = text.split()
    my_dictionary = {}
    tmp_dictionary = {}
    for word in text:
        if word in my_dictionary.keys():
            my_dictionary[word] += 1
            if my_dictionary[word] / len(text) > 0.03 and word not in tmp_dictionary.keys():
                print(f'Word {word} is overly used')
                tmp_dictionary[word] = True
        else:
            my_dictionary[word] =1
    return my_dictionary
#zadanie domowe: ile razy występuje

