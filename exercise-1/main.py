# TODO: don't use random pointless string addition...
def hello_world():
    return "Hello" + ", " + "world!"

# TODO: use a ternary
def greet(name = None):
    if name is None:
        return "Hello, world!"
    else:
        return f"Hello, {name}!"

# TODO: remove if/else hell and general HOW DO I READ THIS-ness
def describe_number(num):
    if num < 0:
        # trying to check for integers
        if num % 2 == 1 and num == int(num):
            # negative and odd
            return { 'is_even': False, 'is_positive': False }
        elif num % 2 == 0 and num == int(num):
            # negative and even
            return { 'is_even': True, 'is_positive': False }
        else:
            # other weird things happening??
            return { 'is_even': False, 'is_positive': False }
    elif num == 0:
        # zero is a weird number
        return { 'is_even': True, 'is_positive': False }
    elif num > 0 and num == int(num):
        if num % 2 == 1:
            # positive and odd
            return { 'is_even': False, 'is_positive': True }
        elif num % 2 == 0:
            # positive and even
            return { 'is_even': True, 'is_positive': True }
        else:
            # other weird things happening??
            return { 'is_even': False, 'is_positive': True }
    else:
        # let's hope for the best here because I don't know what's going on
        return { 'is_even': False, 'is_positive': True }



