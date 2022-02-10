import matplotlib.pyplot as plt

def printResult(x, y):
    print(f'X = {x[-1]}\nL({x[-1]}) = {y[-1]}\n' + '-'*100)
    string = ' x |\t'
    for i in range(len(x)):
        string += str(round(x[i], 1)) + '\t|\t'
    print(string)
    print('-'*100)
    string = ' y |\t'
    for i in range(len(y)):
        string += str(round(y[i], 1)) + '\t|\t'
    print(string)
    print('-'*100)

def Lagrange(x, y):
    curX = x[-1]
    L = 0
    for i in range(len(y)):
        numerator = denominator = 1
        for j in range(len(x)-1):
            if i != j:
                numerator *= curX - x[j]
                denominator *= x[i] - x[j]
        L += y[i] * numerator/denominator
    y.append(L)


x = [2, 2.3, 2.5, 3.0, 3.7, 2.7]
y = [5.8, 6.12, 6.3, 6.7, 7.05]

Lagrange(x, y)

printResult(x, y)


plt.plot(x,y)
plt.show()
