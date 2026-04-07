import random

salary = int(input('Enter your salary: '))
bonus = bool(random.randint(0, 1))

if bonus == 0:
    print(f'{salary}, {bonus} - ${int(salary + random.random())}')
else:
    print(f'{salary}, {bonus} - ${int(salary)}')
