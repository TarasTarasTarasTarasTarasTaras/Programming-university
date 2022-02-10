#include <iostream>
#include <vector>
using namespace std;

void LU_decomposition() {
    cout << "Please enter the number of rows of the matrix: ";
    int n; cin >> n;

    double** arr = new double* [n];
    for (int i = 0; i < n; ++i)
        arr[i] = new double[n];

    cout << "Please enter the matrix of size " << n << 'x' << n << ": \n";

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> arr[i][j];

    vector<double> L;

    for (int i = 1; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            double temp = arr[j][i - 1] / arr[i - 1][i - 1];
            L.push_back(temp);
            for (int k = i - 1; k < n; ++k) {
                arr[j][k] = arr[j][k] - temp * arr[i - 1][k];
                if (arr[j][k] == 0 && k >= j) {
                    cout << "There are no solutions!" << endl;
                    return;
                }
            }
        }
    }

    cout << endl << "======= Matrix U =======" << endl;
    for (int i = 0; i < n; ++i) {
        cout << '[';
        for (int j = 0; j < n; ++j)
            cout << arr[i][j] << '\t';
        cout << ']' << endl;
    }

    cout << endl << "======= Matrix L =======" << endl;
    for (int i = 0, k = 0; i < n; ++i) {
        cout << '[';
        for (int j = 0; j < n; ++j) {
            if (i == j) cout << "1\t";
            else if (j < i) cout << L[k++] << '\t';
            else cout << "0\t";
        }
        cout << ']' << endl;
    }
}


int main() {
    LU_decomposition();
}
