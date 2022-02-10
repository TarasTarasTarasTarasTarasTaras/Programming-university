import numpy as np

def Seidel(A, B, e):
    SIZE = len(A)
    MAX_ITERATION = 1000

    X = [0 for i in range(SIZE)]
    newX = [0 for i in range(SIZE)]

    for iter in range(MAX_ITERATION):
        
        for i in range(SIZE):
            sa = sum(-A[i][j] * newX[j] for j in range(SIZE) if i != j)
            newX[i] = (B[i] + sa)/A[i][i]
            

        if all(abs(newX[j]-X[j]) < e for j in range(SIZE)):
            return newX 
        X=newX[:]
        print('Iteration '+str(iter+1)+':\n' + str(X))
    return "Equations have no solutions"


A = [[0.77, 0.04, -0.21, 0.18],
    [-0.45, 1.23, -0.06, 0.],
    [-0.26, -0.34, 1.11, 0.],
    [-0.05, 0.26, -0.34, 1.12]]

B = [1.24, -0.88, 0.62, -1.17]

e = 0.001

array = Seidel(A,B,e)
print("=" * 30 + "\nSolution:")
print(array)

