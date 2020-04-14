#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    ll t;
    cin >> t;
    while(t--) {
        ll n, x;
        cin >> n;
        vector<ll> v;
        for(ll i=0; i<n; ++i) {
            cin >> x;
            v.push_back(x);
        }
        ll count = 0, start2 = -1, start4 = -1, oddStart = -1;
        for(ll i=0; i<n; ++i) {
            if(v[i]%2!=0) {
                if(i!=0 && v[i-1]%2==0 || (i==0)) {
                    oddStart = i;
                    count += 1;
                }
                else if(v[i-1]%2!=0) {
                    count += i - oddStart + 1;
                }
                if(start4 != -1) {
                    count += start4 + 1;
                }
            }
            else {
                if(v[i]%4 == 0) {
                    start4 = i;
                }
                else if(start2 != -1 && start2 > start4) {
                    start4 = start2;
                }
                start2 = i;
                
                if(start4 != -1) {
                    count += start4 + 1;
                }
            }
        }
        cout << count << "\n";
    }
    return 0;
}