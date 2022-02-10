import sympy as sp
import numpy as np

def calculate_the_integral(a, b, func):
    integrate_func = sp.integrate(func, sp.Symbol('x'))
    result = integrate_func.subs(sp.Symbol('x'), b) - integrate_func.subs(sp.Symbol('x'), a)
    return result


def func_derivative(func, number):
    for i in range(number):
        func = sp.diff(func, 'x')
    return func


def find_max(a, b, func):
    result = max(abs(sp.minimum(func, sp.Symbol('x'), sp.Interval(a, b))), 
                 abs(sp.maximum(func, sp.Symbol('x'), sp.Interval(a, b))))
    return result


def rectangle(a, b, func, e):
    function_derivative = func_derivative(func, 2)
    m = find_max(a, b, function_derivative)
    n = round((b-a)*(((b-a)*m/12/e)**0.5))
    h = (b - a) / n
    s = 0.0

    for i in range(n):
        x = a + i * h
        s = s + sp.sympify(func).subs(sp.Symbol('x'), x)
    result = s * h
    return [result, n]


def trapeze(a, b, func, e):
    function = sp.sympify(func)
    function_derivative = func_derivative(func, 2)
    m = find_max(a, b, function_derivative)
    n = round((b-a)*(((b-a)*m/12/e)**0.5))
    h = (b - a) / n
    s = 0.0

    for i in range(n-1):
        x = a + i * h
        s = s + function.subs(sp.Symbol('x'), x)
    result = (h / 2) * (function.subs(sp.Symbol('x'), a) + function.subs(sp.Symbol('x'), b) + 2 * s)
    return [result, n-1]


def parabola(a, b, func, e):
    function = sp.sympify(func)
    function_derivative = func_derivative(func, 4)
    m = find_max(a, b, function_derivative)
    n = round((b-a)*(((b-a)*m/180/e)**0.25))
    h = (b - a) / n
    s1 = 0.0
    s2 = 0.0
    
    for i in range(n-1):
        x = a + i * h
        if i % 2 != 0: s1 += function.subs(sp.Symbol('x'), x)
        else:          s2 += function.subs(sp.Symbol('x'), x)
    result = (h / 3) * (function.subs(sp.Symbol('x'), a) + function.subs(sp.Symbol('x'), b) + 4 * s1 + 2 * s2)
    return [result, n-1]


def main():
    func = "sqrt(6*x-5)"
    a = 3.0
    b = 9.0
    e = 0.001
    print(calculate_the_integral(a,b,func), '\n')

    rectangle_ = rectangle(a, b, func, e)
    print(f'--Rectangle method--  [Iterations: {rectangle_[1]}]. Result: {rectangle_[0]}\n')
    trapeze_ = trapeze(a, b, func, e)
    print(f'  --Trapeze method--  [Iterations: {trapeze_[1]}]. Result: {trapeze_[0]}\n')
    parabola_ = parabola(a, b, func, e)
    print(f' --Parabola method--  [Iterations: {parabola_[1]}]. Result: {parabola_[0]}\n')


if __name__ == '__main__':
    main()