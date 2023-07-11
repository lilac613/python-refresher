import numpy as np


def hello():
    return "Hello, world!"


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero!")
    return a / b


def sqrt(a):
    return np.sqrt(a)

def power(a, b):
    return np.power(a, b)

def log(a):
    return np.log(a)

def exp(a):
    return np.exp(a)

def sin(a):
    return np.sin(a)

def cos(a):
    return np.cos(a)

def tan(a):
    return np.tan(a)

def cot(a):
    return 1 / np.tan(a)

def __main__():
    hello()


if __name__ == "__main__":
    __main__()

# test functions
print(add (3,5))
print(add (-3,-5))
print(add(-3,5))

print(sub (3,5))
print(sub (-3,-5))
print(sub (-3,5))

print(mul (3,5))
print(mul (-3,-5))
print(mul (-3,5))

print(div (3,5))
print(div (0,5))
print(div (5,0))

print(sqrt(-4))
print(sqrt(4))
print(sqrt(25))

print(power(2,3))
print(power(-2,3))
print(power(2,-3))

print(log(0))
print(log(1))
print(log(100))

print(exp(3))
print(exp(0))
print(exp(-3))

print(sin(0))
print(sin(3.14/2))
print(sin(3.14*1.5))

print(cos(0))
print(cos(3.14/2))
print(cos(3.14*1.5))

print(tan(0))
print(tan(3.14/2))
print(tan(3.14))

print(cot(0))
print(cot(3.14/2))
print(cot(3.14))

