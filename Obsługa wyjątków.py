name_dictionary = {
    'Jan': 'John',
    'Maria': 'Marry',
    'Jacek': 'Jack'
}

x = input('Enter two numbers to be divided: ').split()

try:
    result = int(x[0]) / int(x[1])
except IndexError:
    print('Error. Too few numbers')
    result = int(x[0])
except ZeroDivisionError:
    print('Error. Division by zero.')
    result = 0
    raise
except ValueError:
    print('Error. Invalid number.')
    result = 0
else:
    print(f'Operation successful. Log file is being created..')
finally:
    print('Finally - end')
    print(f'Result is {result}')

print(result)
