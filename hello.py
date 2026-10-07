import os
import sys


def greet(name):
    var_greeting = "Hello, " + name    # code smell: should use f-string
    print(var_greeting)


def add(a, b):
    result = a + b
    return result


def divide(a, b):
    return a / b   # potential bug: no zero check


def unused_helper():
    x = 42         # unused variable
    return x


def main():
    greet("SonarQube")
    print(add(5, 10))
    print(divide(10, 2))

    numbers = [1, 2, 3, 4, 5]
    total = 0
    for n in numbers:
        total = total + n
    print("Total:", total)


if __name__ == "__main__":
    main()
