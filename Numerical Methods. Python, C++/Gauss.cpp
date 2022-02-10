#include <iostream>
#include <vector>
using namespace std;

vector<double> Gauss() {
    cout << "Please enter the number of rows of the matrix: ";
    int n; cin >> n;
    int m = n + 1;

    double** arr = new double* [n];
    for (int i = 0; i < n; ++i)
        arr[i] = new double[m];

    cout << "Please enter the matrix of size " << n << 'x' << m << ": \n";

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> arr[i][j];

    vector<double> L;
    vector<double> x(n, 0);

    for (int i = 1; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            double temp = arr[j][i - 1] / arr[i - 1][i - 1];
            L.push_back(temp);
            for (int k = i - 1; k < m; ++k) {
                arr[j][k] = arr[j][k] - temp * arr[i - 1][k];
                if (arr[j][k] == 0 && k >= j) {
                    cout << "There are no solutions!" << endl;
                    return x;
                }
            }
        }
    }

    for (int i = n - 1, k = 1; i >= 0; --i, ++k) {
        x[i] = arr[i][n] / arr[i][n - k];
        for (int j = 0; j < n; ++j)
            arr[j][n] -= x[i] * arr[j][i];
    }

    for (int i = 0; i < n; ++i)
        cout << "x[" << i << "] = " << x[i] << '\n';

    return x;
}

int main() {
    Gauss();
}
