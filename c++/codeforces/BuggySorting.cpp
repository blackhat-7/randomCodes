#include <bits/stdc++.h>
using namespace std;
// #define ll long long

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    if(n <= 2) {
        cout << "-1\n";
    }
    else {
        for(int i=1; i<n; ++i) {
            cout << 100 << " ";
        }
        cout << "1\n";
    }
}