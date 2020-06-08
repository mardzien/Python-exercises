def func():
    return 1


def hello():
    return "Hello!"


greet = hello

print(greet())


# returning function
def hello(name='Martin'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print('I am going to return a function...')

    if name == 'Martin':
        return greet
    else:
        return welcome


my_new_function = hello('Martin')
print(my_new_function())


# passing function as an argument

def hello():
    return "Hello there!"


def other_function(some_function):
    print('Executing other function.')
    print(some_function())


other_function(hello)


def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function')

    return wrap_func


def func_needs_decorator():
    print("I want to be decorated.")


decorated_func = new_decorator(func_needs_decorator)

decorated_func()

# decorator syntax
@new_decorator
def func_needs_decorator():
    print("I want to be decorated.")


func_needs_decorator()
