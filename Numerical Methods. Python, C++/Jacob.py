import numpy as np


def Jacobi(A, B, e):
	SIZE = len(A)
	MAX_ITERATION = 1000
	formulas = [[0 for i in range(SIZE)] for j in range(SIZE)]

	for i in range(SIZE) :
		k = -1
		for j in range(SIZE):
			if i == j:
				formulas[i][SIZE-1] = B[i] / A[i][i]
			else:
				k+=1
				formulas[i][k] = A[i][j] / A[i][i] * -1

	X = []
	for i in range(SIZE):
		X.append(formulas[i][SIZE-1])

	for i in range(MAX_ITERATION):
		newX = [0 for j in range(SIZE)]
		for j in range(SIZE):
			k = -1
			for m in range(SIZE):
				if j == m:
					newX[j] += formulas[j][SIZE-1]
				else:
					k+=1
					newX[j] += formulas[j][k] * X[m]

		print("Iteration number " + str(i + 1) + ":  " + str(newX))
		difference = np.absolute(abs(np.array(newX) - np.array(X)))
		print("   Difference: ", difference)
		if np.allclose(X, newX, atol = 0.00001):
			return newX
		X = newX[:]


def strArray(array):
	string = "[ "
	for i in array:
		i = round(i, 6)
		string += str(i) + " "
	string += " ]"
	return string



A = [
    [10., 5., 3., -4],
    [3., 7., -2., 0 ],
    [5., -7., 10., 0],
	[0., 3., 0., -5,]]

B = [20., 9., -9., 1.]

e = 0.001

ARRAY = Jacobi(A,B,e)

print("\n           Solution: " + strArray(ARRAY))
