#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll t;
    cin >> t;
    while(t--) {
        ll n, m, k, x;
        cin >> n >> m >> k;
        ll c[n][m];
        for(ll i=0; i<n; ++i) {
            for(ll j=0; j<m; ++j) {
                c[i][j] = 0;
            }
        }
        for(ll i=0; i<n; ++i) {
            for(ll j=0; j<k; ++j) {
                cin >> x;
                ++c[i][x-1];
            }
        }
        for(ll i=0; i<n; ++i) {
            cout << distance(c[i], max_element(c[i], c[i] + m)) + 1 << " ";
        }
        cout << "\n";
    }
    return 0;
}