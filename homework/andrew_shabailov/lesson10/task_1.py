def decor_func(func):

    def wrapper():
        func()
        print('finished')
    return wrapper


@decor_func
def good():
    print('good')


good()
