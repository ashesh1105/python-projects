def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x * y

# Floor division
def divide_floor(x, y):
    if y ==  0:
        raise ValueError('Can not devide by zero!')

    # Using floor division for now, i.e, result will be rounded down to an int. 5/2 = 2 and not 2.5
    return x // y

# Regular division
def divide(x, y):
    if y ==  0:
        raise ValueError('Can not devide by zero!')
    return x/y



