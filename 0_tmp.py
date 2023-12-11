my_string = 'Mum.has.bought.a.dog.'

splitted_string = my_string.split('.')
print(my_string)
print(f'Unsplitted string: { my_string}')
print(f'Splitted string {splitted_string}')

print('\nDeleteing characters')
my_string = 'Mum.has.bought.a.dog.'
my_string = my_string.replace('.', '')
print(f'String with periods removed: {my_string}')


print('\nFunctions')
special_characters = []
def after_a(text):
    return text[text.index('a')+1]
my_string = 'Mum.has.bought.a.dog.'
print(after_a(my_string))


print('\nSets')
set1 = {'.', ',', '('}
set2 = set('.,:(){}[]!')
print(f'Set 2: {set2}')
set3 = set('.,(\'\"\\')
print(f'Set 3: {set3}')


#print('\nArgs')
#def draw_lines(x, y, *coordinates):
#    start = [x, y]
#    for i in range(0, len(coordinates), 2):
#        print(f'Lime is being drawn from {start} to {coordinates[i]}, {coordinates[i +1]}')
#        start = [coodinates[i], coordinates[i + 1]]

#draw_lines(1, 1, 5, 6, 8, 9)


def triangle(**data):
    if 'a' in data.keys and 'b' in data.keys() and 'c' in data.keys():
        print(f'Triangle is calculated based on three sides')
    elif 'a' in data.keys() and 'b' in data.keys() and 'alpha' in data.keys():
        print(f'Triangle is calculated based on two sides and an angle')
    elif 'a' in data.keys() and 'alpha' in data.keys() and 'beta' in data.keys():
        print(f'Triangle is calculated based on one side and two angles')
    elif 'a' in data.keys() and 'h' in data.keys():
        print(f'Triangle is calculated based on one side and height')
    else:
        print('Insufficient data')

triangle(5,3,23)
