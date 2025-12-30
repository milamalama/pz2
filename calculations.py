import math

def linear(x):
    return 2 * x + 3

def quadratic(x):
    return x ** 2 - 4 * x + 3

def sine(x):
    return math.sin(x)

def exponential(x):
    return math.exp(x)

def logarithm(x):
    if x <= 0:
        raise ValueError("Аргумент логарифма должен быть > 0")
    return math.log(x)
