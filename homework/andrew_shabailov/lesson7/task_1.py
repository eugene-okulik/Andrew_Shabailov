# Case 1
# user_input = int(input('Enter a number to guess: '))
#
# while user_input != 2:
#     print('Please, try again')
#     user_input = int(input('Enter a number to guess: '))
# print('Congratulations! You guessed the number!')


# Case 2
user_input = int(input('Enter a number to guess: '))

while True:
    if user_input != 2:
        print('Please, try again')
        user_input = int(input('Enter a number to guess: '))
        continue
    if user_input == 2:
        print('Congratulations! You guessed the number!')
        break
