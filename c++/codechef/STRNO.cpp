#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void primeFactors(int n, vector<ll> &factors)  
{
    while (n % 2 == 0)  
    {  
        factors.push_back(2);
        n = n/2;  
    }  
    for (int i = 3; i <= sqrt(n); i = i + 2)  
    {  
        while (n % i == 0)  
        {  
            factors.push_back(i);  
            n = n/i;  
        }  
    }  
    if (n > 2)  
        factors.push_back(n);
}

int main() {
    ll t;
    cin >> t;
    while(t--) {
        ll x, k;
        cin >> x >> k;
        vector<ll> factors;
        primeFactors(x, factors);
        if(k <= factors.size() || (k == 1 && x != 1)) {
            cout << "1\n";
        }
        else {
            cout << "0\n";
        }
    }
    return 0;
}