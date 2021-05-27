#include <iostream>
using namespace std;

int main() {
    size_t t;
    cin >> t;
    for (size_t k = 0; k < t; k++) {
        long long n, m, x;
        cin >> n >> m >> x;
        long long j = (x - 1) / n;
        long long i = (x - 1) % n;
        cout << i*m + j + 1 << '\n';
    }
    cout << flush;
    return 0;
}