#debugger

def sample(x):
    return x + 1

a = 0
for i in range(10):
    a += 1
    number = sample(a)
    print(f'Iteration {i + 1}')
    print(f'a = {a}')
    if a == 3:
        continue
    if a == 5:
        break
    print('Iteration ended')
print('Loop ended')
