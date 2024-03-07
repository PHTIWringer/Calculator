import math
import sympy as sp


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

## CALCULATE THE DERIVATIVE ##

def calculate_derivative(func, var):
    derivative = sp.diff(func, var)
    return derivative

x = sp.symbols('x')  # Define a symbolic variable
f = x**2 + 3*x + 2  # Define a function of x

# Calculate the derivative
df = calculate_derivative(f, x)
print(df)

## DERIVATIVE IN EASIER EXPRESSIONS ##

def calculate_derivative_main(func_str, var_str):
    """
    Calculate the derivative of a function provided as a string.

    Parameters:
    func_str (str): The function to differentiate as a string.
    var_str (str): The variable with respect to which to differentiate as a string.

    Returns:
    sympy expression: The derivative of the function.
    """
    var = sp.symbols(var_str)  # Convert the variable string to a sympy symbol
    func = sp.sympify(func_str)  # Convert the function string to a sympy expression
    derivative = sp.diff(func, var)
    return derivative

# Example usage
func_str = "x^2 + 3*x + 2"
var_str = "x"
derivative = calculate_derivative_main(func_str, var_str)
print(derivative)
