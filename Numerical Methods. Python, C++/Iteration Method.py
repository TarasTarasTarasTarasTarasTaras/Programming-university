from copy import deepcopy
from sympy import Symbol, diff, sin, sqrt, asin, sympify


def IterationMethod(f1, f2, x0, y0, e, x, y):
    f1_dx = diff(f1, x)
    f1_dy = diff(f1, y)
    f2_dx = diff(f2, x)
    f2_dy = diff(f2, y)

    if (abs(f1_dx.subs({x: x0, y: y0})) + abs(f1_dy.subs({x: x0, y: y0})) >= 1 or
        abs(f2_dx.subs({x: x0, y: y0})) + abs(f2_dy.subs({x: x0, y: y0})) >= 1):
        return 'The system has no solutions'

    print('-'*22+'IterationMethod'+'-'*22)

    for i in range(1000):
        currentX = deepcopy(x0)
        currentY = deepcopy(y0)

        x0 = f1.subs({x: currentX, y: currentY})
        y0 = f2.subs({x: currentX, y: currentY})
        print('Iteration no ' + str(i + 1) + ': x: ' + str(x0) + '   y: ' + str(y0))
        if (abs(currentX - x0) <= e and abs(currentY - y0) <= e):
            break

    return 'x = ' +str(x0) + ',  y = ' +str(y0)


def main():
    f1 = sympify(input('Enter function 1: '))
    f2 = sympify(input('Enter function 2: '))

    x0 = float(input("Enter x0: "))
    y0 = float(input("Enter y0: "))
    e = float(input("Enter e: "))

    result = IterationMethod(f1, f2, x0, y0, e, Symbol('x'), Symbol('y'))
    print ('-'*59,'\n RESULT: '+str(result))



if __name__ == "__main__":
    main()