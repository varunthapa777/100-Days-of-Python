def add(*args):
    for n in args:
        print(n)


def calculate(n, **kwargs):
    n += kwargs.get("add")
    n *= kwargs.get("multipy")
    n -= kwargs.get("sub") if kwargs.get("sub") is not None else 0
    print(n)


calculate(5, add=5, multipy=3)

