#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

typedef long long ll;

void solve()
{
    std::cout << "Hello World" << std::endl;
    ll n;
    std::cin >> n;
    ll arr[n];
    for (ll i=0; i<n; i++) {
        std::cin >> arr[i];
    }
    std::sort(arr, arr+n);
    for (ll i=0; i<n; i++) {
        if ((i == 0 || abs(arr[i]-arr[i-1]) > 1) && (i == n-1 || abs(arr[i]-arr[i+1]) > 1)) {
            if (i==0 && i ==n-1) break;
            std::cout << "NO\n";
            return;
        }
    }
    std::cout << "YES\n";
}


int main()
{
    ll t;
    std::cin >> t;
    while (t--) {
        solve();
    }
}
