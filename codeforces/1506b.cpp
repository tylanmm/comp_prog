#include <iostream>
#include <string>
using namespace std;

int main() {
    int t; cin >> t;
    for (int _t = 0; _t < t; _t++) {
        int n, k; cin >> n >> k;
        char s[n]; cin >> s;
        
        // find first
        int st = 0;
        for ( ; st < n; st++)
            if (s[st] == '*')
                break;

        // find last
        int f = n - 1;
        for ( ; f > -1; f--)
            if (s[f] == '*')
                break;

        int res = (st == f) ? 1 : (st == n) ? 0 : 2;
        int i = st, last = st;
        for (int j = st+1; j < f; j++) {
            if (j - i > k) {
                i = last;
                res++;
            }
            
            if (s[j] == '*')
                last = j;
        }

        cout << res << '\n';
    }
    
    cout << flush;
    return 0;
}