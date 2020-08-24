#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll t, n, x;
    cin >> t;
    while(t--) {
        bool firstPerson = true, socialDistancing = true;
        ll space = 0;
        cin >> n;
        int prevPersonIndex;
        for(ll i=0; i<n; ++i) {
            cin >> x;
            if(x==1) {
                if (!firstPerson && i-prevPersonIndex < 6) {
                    socialDistancing = false;
                }
                firstPerson = false;
                prevPersonIndex = i; 
            }

        }
        if(socialDistancing) {
            cout << "YES\n";
        }
        else {
            cout << "NO\n";
        }
    }
    return 0;
}