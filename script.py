import math

## BASIC ADDITION ##

def basic_sum(a, b):
    c = a + b
    return c

print(basic_sum(5, 5))

## BASIC ADDITION INFINITE NUMBER'S ##

def int_sum(*args):
    return sum(args)

print(int_sum(5, 5, 5))

## BASIC SUBTRACTION ##

def basic_sub(a, b):
    c = a - b
    return c

print(basic_sub(5, 15))

## BASIC SUBTRACTION INFINITE NUMBER'S ##

def subtract(num):
    if not num:
        return 0
    
    result = num[0]
    for number in num[1:]:
        result -= number
    
    return result

numbers = [10, 4, 3]
result = subtract(numbers)
print(result)