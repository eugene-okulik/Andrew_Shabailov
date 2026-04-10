def repeat_func(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat_func(5)
def good():
    print('good_task')


good()