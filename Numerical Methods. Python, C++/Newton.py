import numpy as np
from sympy import Symbol, diff, symbols, cos, sin, tan

def Newton(x, y, e, f1, f2):
    iter_limit = 100
    
    f1_dx = lambda x,y : -2*x + y*sin(x*y+0.1)**2/cos(x*y + 0.1)**2 + y
    f2_dx = lambda x,y : 2*x
    f1_dy = lambda x,y : x*sin(x*y + 0.1)**2/cos(x*y + 0.1)**2 + x
    f2_dy = lambda x,y : 4*y

    for i in range(iter_limit):
        dx = f1(x, y) * f2_dy(x, y) - f2(x, y) * f1_dy(x, y)
        dy = f2(x, y) * f1_dx(x, y) - f1(x, y) * f2_dx(x, y)

        print('Iteration ' + str(i+1) + '\nX: ' +str(x) + '  Y: ' + str(y))
        if abs(dx) < e or abs(dy) < e:
            result = {"y": y, "x": x};
            return result

        diff = f1_dx(x, y) * f2_dy(x, y) - f1_dy(x, y) * f2_dx(x, y)
        
        x -= dx / diff
        y -= dy / diff
        print('===================')

    print("\nThere are no solutions")
    return None



def main():
    f1 = lambda x, y: tan(x*y-x**2) + x*y - 0.3
    f2 = lambda x, y: x**2 + y**2 - 1.5

    x0 = 0.65
    y0 = 0.5
    e = 0.001

    res = Newton(x0, y0, e, f1, f2)
    if res is not None:
        print('\n\nResult:\n   X: ' + str(res["x"]) +  'Y: ' + str (res["y"]))



if __name__ == "__main__":
    main()
