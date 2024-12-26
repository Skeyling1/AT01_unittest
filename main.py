def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b


def even(a):
    if a % 2 == 0:
        return True
    else:
        return False


#Написать функцию для вычисления остатка от деления и тесты для проверки её работы, включая обработку деления на ноль
def reminder_from_division(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    else:
        return a % b


