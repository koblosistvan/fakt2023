/*Nemes Tihamér Online 2. forduló - 2. feladat - Nomád játék
Kadarkuti Márton */

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // bemenet
    int osszeg;
    int a;
    int b;
    int m; //megoldasok szama
    vector<int> x_megold;
    vector<int> y_megold;

    cin >> osszeg;
    cin >> a;
    cin >> b;

    for (int x = 0; x < 1+ osszeg/a; x++) {
        for (int y = 0; y < 1+ osszeg/b; y++) {
            if (a*x + b*y == osszeg) {
                m++;
                x_megold.push_back(x);
                y_megold.push_back(y);
            }
        }
    }
    cout << m << "\n";
    for (int i = 0; i<m; i++) {
        cout << x_megold[i] << " " << y_megold[i] << "\n";
    }

    return 0;
}
