def my_function(a, b, c=1):
    if b > a:
        return b + c
    else:
        return a + c
print(my_function(3,5))


def my_arg_finction(*args):
    print(args[2])
    for arg in args:
        if arg > 0:
            print(f'{arg} * 2 is {arg * 2}')
        else:
            print(f'{arg} is lower than zero.')

my_arg_finction(3,4,5,-1,2)


def my_kwargs_function(**kwargs):
    if 'family_name' in kwargs and kwargs['family_name'] == 'Kowalski':
        print('You are blacklisted')

my_kwargs_function(first_name='Kamil', family_name='Kowalski', status='single')



#print('\nArgs')
#def draw_lines(x, y, *coordinates):
#    start = [x, y]
#    for i in range(0, len(coordinates), 2):
#        print(f'Lime is being drawn from {start} to {coordinates[i]}, {coordinates[i +1]}')
#        start = [coodinates[i], coordinates[i + 1]]

#draw_lines(1, 1, 5, 6, 8, 9)


#def triangle(**data):
#    if 'a' in data.keys and 'b' in data.keys() and 'c' in data.keys():
#        print(f'Triangle is calculated based on three sides')
#    elif 'a' in data.keys() and 'b' in data.keys() and 'alpha' in data.keys():
#        print(f'Triangle is calculated based on two sides and an angle')
#    elif 'a' in data.keys() and 'alpha' in data.keys() and 'beta' in data.keys():
#        print(f'Triangle is calculated based on one side and two angles')
#    elif 'a' in data.keys() and 'h' in data.keys():
#        print(f'Triangle is calculated based on one side and height')
#    else:
#        print('Insufficient data')

#triangle(5,43,23)


login_database = ['Kamilxxx', 'Marzenka78', 'Ola123']

def check_logins(*logins):
    available_login_list = []
    for login in logins:
        if login not in login_database:
            print(f'Login {login} is available')
            available_login_list.append(login)
    return available_login_list
print(check_logins('Kamil', 'Kamilxxx', 'Ola', 'Ola123'))

def final_function(b, a=1, c=0):
    return a + b + c


print(final_function(3,4))


def final_function2(a, b, *rest):
    return True
