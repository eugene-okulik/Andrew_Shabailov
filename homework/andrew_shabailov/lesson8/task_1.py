import random

salary = int(input('Enter your salary: '))
print(f'Yor salary with bonus: {salary}, bonus: {bool(random.randint(0, 1))}')
