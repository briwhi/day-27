def add(*args):
    total = 0
    for num in args:
        total += num

    print(total)

add(5,6,7,8)


def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)



calculate(add=3, multiply=5)
