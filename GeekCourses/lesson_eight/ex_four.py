from functools import wraps


def val_checker(check):
    def _val_checker(f_calc):
        @wraps(f_calc)
        def callback(x):
            if check(x):
                return f_calc(x)
            else:
                return ValueError(f'Wrong value {x}')
        return callback
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    '''calc_cube'''
    return x ** 3

value = calc_cube(-5)
print(value)
