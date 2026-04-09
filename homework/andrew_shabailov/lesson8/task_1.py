import random

salary = int(input('Enter your salary: '))
bonus = random.choice([True, False])

if bonus:
    print(f'{salary}, {bonus} - ${int(salary + random.random())}')
else:
    print(f'{salary}, {bonus} - ${int(salary)}')
