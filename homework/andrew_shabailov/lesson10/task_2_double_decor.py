def decor_twice(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@decor_twice
def good():
    print('good')


good()
