#include <bits/stdc++.h> 
#include <utility>
#include <iomanip>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>
#include <set>

using namespace std; 
#define ll long long

void addEdge(vector<ll> adj[], ll u, ll v) 
{ 
    adj[u].push_back(v); 
    adj[v].push_back(u); 
} 

ll mod = 1000000007; 

ll mult(ll a, ll b) 
{ 
    return ((a % mod) *  
        (b % mod)) % mod; 
}

ll binpower(ll a, ll n, ll mod) {
	ll p = 1;
	while (n > 0) {
		if(n%2) {
			p = p * a; p %= mod;
		} 
		n >>= 1; a *= a; a %= mod;
	} 
	return p % mod;
}

bool check_composite(ll n, ll a, ll d, ll s) {
    ll x = binpower(a, d, n);
    if (x == 1 || x == n - 1)
        return false;
    for (ll r = 1; r < s; r++) {
        x = x * x % n;
        if (x == n - 1)
            return false;
    }
    return true;
};

bool MillerRabin(ll n) { // returns true if n is prime, else returns false.
    if (n < 2)
        return false;

    ll r = 0;
    ll d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        r++;
    }

    for (ll a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        if (n == a)
            return true;
        if (check_composite(n, a, d, r))
            return false;
    }
    return true;
}
  
ll primes[1000006];

ll divisorCount(ll n) { // returns number of divisors
	vector<ll> p;
	for(ll i = 2; i < 1000006; i++) {
		if(primes[i]) continue;
		p.push_back(i);
		for(ll j = i*i; j < 1000006; j += i) {
			primes[j] = 1;
		}
	}
	ll ans = 1;
	for(ll i: p) {
		if(i*i*i > n) break;
		ll count = 1;
		while(n%i == 0) {
			n /= i;
			count++;
		}
		ans = mult(ans, count);
	}
	if(MillerRabin(n)) ans = mult(ans, 2);
	else {
		ll x = sqrtl(n);
		if(x*x == n && MillerRabin(x)) ans = mult(ans, 3);
		else if(n != 1) ans = mult(ans, 4);
	}
	return ans % mod;
}

void storeProducts(vector<ll> productMatrix[], int n, vector<ll> adj[]) {
    for(int i=0; i<n; ++i) {
        for(int j=0; j<adj[i].size(); ++j) {
            productMatrix[i][adj[i][j]] = productMatrix[i][i] * productMatrix[j][j];
        }
    }
}

ll bfs(vector<ll> adj[], ll n, ll u, ll v, vector<ll> productMatrix[]) 
{
    ll curr;
    queue<ll> q;
    bool visited[n];
    for(ll i=0; i<n; ++i) {
        visited[i] = false;
    }
    visited[u] = true;
    q.push(u);
  
    while (!q.empty()) { 

        ll f = q.front();
        if(f == v) {
            break;
        }
        q.pop();
        for (ll i=0; i < adj[f].size(); ++i) {
            curr = adj[f][i];
            if(!visited[curr]) {
                productMatrix[u][curr] = max(productMatrix[u][f], productMatrix[f][u]) * productMatrix[curr][curr];
                q.push(curr); 
                visited[curr] = true;
            }
        } 
    } 
    for(int i=0; i<n; ++i) {
        for(int j=0; j<n; ++j) {
            cout << productMatrix[i][j] << " ";
        }
        cout << "\n";
    }
    return productMatrix[u][v];
}

int main() {
    ll t;
    cin >> t;
    while(t--) {
        ll n, q, x, y, u, v, ans, quotient;
        cin >> n;
        vector<ll> adj[n];
        vector<ll> productMatrix[n];
        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; ++j) {
                productMatrix[i].push_back(-1);
            }
        }
        for(ll i=0; i<n-1; ++i) {
            cin >> x >> y;
            addEdge(adj, x-1, y-1);
        }
        for(ll i=0; i<n; ++i) {
            cin >> productMatrix[i][i];
        }
        cin >> q;
        for(ll i=0; i<q; ++i) {
            cin >> u >> v;
            quotient = bfs(adj, n, u-1, v-1, productMatrix);
            ans = divisorCount(quotient);
            cout << ans << "\n";
        }
    }
    return 0;
}