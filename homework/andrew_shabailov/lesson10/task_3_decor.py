first = int(input("Enter first number: "))
second = int(input("Enter second number: "))


def user_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@user_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


print(calc(first, second))
