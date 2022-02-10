from math import sqrt
import numpy as np
import cmath

def Cholesky_decomposition(A):
    n = len(A)
    L = [[0j for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i+1):
            temp = sum(L[i][k] * L[j][k] for k in range(j))
            difference = A[i][i] - temp
            if (i == j):
                L[i][j] = difference ** 0.5
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - temp))
    return L


def get_U_matrix(L):
    n = len(L)
    U = [[0j for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                U[i][j] = L[i][j]
            elif i < j:
                U[i][j] = L[j][i]
            else:
                U[i][j] = 0
    return U


def getResultCholesky(A, L, B):
    n = len(A)
    U = get_U_matrix(L)

    resultX = [0j for i in range(n)]
    resultY = [0j for i in range(n)]


    for i in range(n):
        temp = sum(U[j][i] * resultY[j] for j in range(i))
        resultY[i] = (B[i] - temp) / U[i][i]

    for i in range(n-1, -1, -1):
        temp = sum(U[i][j] * resultX[j] for j in range(i+1, n))
        resultX[i] = (resultY[i] - temp) / U[i][i]

    return resultX


'''
A = [[4,2,2,1],
     [2,5,1,2],
     [2,1,5,1],
     [1,2,1,4.875]]

B = [9,10,9,8.875] 
'''

A = [[2.45,1.75,-3.24],
     [1.75,-1.16,2.18],
     [-3.24,2.18,-1.86]]

B = [1.23,3.43,-0.16]


L = Cholesky_decomposition(A)
U = get_U_matrix(L)

print('A:')
for row in A:
    print(row)

print('\nB:')
print(B)


print('\nL:')
for row in L:
    print(row)

print('\nU:')
for row in U:
    print(row)


print('-'*40)
print('result: ' + str(getResultCholesky(A, L, B)))