#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
    ll t;
    cin >> t;
    while(t--) {
        ll n;
        cin >> n;
        ll arr[n];
        for(ll i=0; i<n; ++i) {
            cin >> arr[i];
        }
        sort(arr, arr+n, greater<>());
        ll sum = 0;
        for(ll i=0; i<n; ++i) {
            if (arr[i] - i <= 0) {
                break;
            }
            sum += arr[i] - i;
        }
        ll ans = sum % (ll)(pow(10, 9)+7);
        cout << ans << "\n";
    }    
    return 0;
}