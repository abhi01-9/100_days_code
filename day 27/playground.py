def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 4, 6))


def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") # if there is no argument .get will return none not an error


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


def test(*args):
    print(args)


test(1, 2, 3, 4)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)

