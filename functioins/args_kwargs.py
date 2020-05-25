def myfunc(*args):
    return sum(args)


print(myfunc(40, 60, 100, 1))


def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("I did not find any fruit here")


myfunc2(fruit='apple', vegetable='carrot')


def myfunc3(*args, **kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")


myfunc3(10, 20, 30, 40, fruit='orange', food='eggs', animal='dog')
