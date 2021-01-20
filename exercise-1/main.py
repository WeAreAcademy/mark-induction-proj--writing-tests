def hello_world():
    return "Hello" + ", " + "world!"

# TODO: use a ternary
def greet(name = None):
    if name is None:
        return "Hello, world!"
    else:
        return f"Hello, {name}!"

# TODO: remove if/else hell
def describe_number(num):
    # Negative numbers
    if num < 0:
        if num % 2 == 1:
            # negative and odd
            return { 'is_even': False, 'is_positive': False }
        elif num % 2 == 0:
            # negative and even
            return { 'is_even': True, 'is_positive': False }
        else:
            # other weird things happening??
            return { 'is_even': False, 'is_positive': False }
    elif num == 0:
        # zero is a weird number
        return { 'is_even': True, 'is_positive': False }
    elif num > 0:
        if num % 2 == 1:
            # positive and odd
            return { 'is_even': False, 'is_positive': True }
        elif num % 2 == 0:
            # positive and even
            return { 'is_even': True, 'is_positive': True }
        else:
            # other weird things happening??
            return { 'is_even': False, 'is_positive': True }


