user_input = int(input('Enter a number to guess: '))

while True:
    if user_input != 2:
        print('Please, try again')
        user_input = int(input('Enter a number to guess: '))
        continue
    if user_input == 2:
        print('Congratulations! You guessed the number!')
        break
