#include <bits/stdc++.h> 
using namespace std; 
typedef long long ll;

void addEdge(vector<ll> adj[], ll u, ll v) 
{ 
    adj[u].push_back(v); 
    adj[v].push_back(u); 
} 

void SieveOfEratosthenes(ll n, bool prime[], bool primesquare[], ll a[]) { 
    for (ll i = 2; i <= n; i++) 
        prime[i] = true; 
    for (ll i = 0; i <= (n * n + 1); i++) 
        primesquare[i] = false; 
  
    prime[1] = false; 
  
    for (ll p = 2; p * p <= n; p++) { 
        if (prime[p] == true) { 
            for (ll i = p * 2; i <= n; i += p) 
                prime[i] = false; 
        } 
    } 
  
    ll j = 0; 
    for (ll p = 2; p <= n; p++) { 
        if (prime[p]) { 
            a[j] = p; 
            primesquare[p * p] = true; 
            j++; 
        } 
    } 
} 
ll countDivisors(ll n) 
{ 
    if (n == 1) 
        return 1; 
  
    bool prime[n + 1], primesquare[n * n + 1]; 
  
    ll a[n];
    SieveOfEratosthenes(n, prime, primesquare, a); 
    ll ans = 1; 
  
    for (ll i = 0;; i++) { 
        if (a[i] * a[i] * a[i] > n) 
            break; 
        ll cnt = 1; 
        while (n % a[i] == 0)
        { 
            n = n / a[i]; 
            ++cnt;
        } 
        ans = ans * cnt; 
    } 

    if (prime[n]) 
        ans = ans * 2; 

    else if (primesquare[n]) 
        ans = ans * 3; 
  
    else if (n != 1) 
        ans = ans * 4; 
  
    return ans;
}

ll bfs(vector<ll> adj[], ll n, ll u, ll v, ll countFactors[]) 
{
    ll sumFactors = countFactors[u], curr;
    queue<pair<ll,ll>> q;
    ll visited[n];
    q.push(make_pair(u, sumFactors));
    visited[u] = true;
  
    while (!q.empty()) { 
  
        pair<ll, ll> f = q.front();
        sumFactors = f.second;
        if(f.first == v) {
            break;
        }
        q.pop();
        for (ll i=0; i < adj[f.first].size(); ++i) {
            curr = adj[f.first][i];
            q.push(make_pair(curr, sumFactors + countFactors[curr])); 
            visited[curr] = true;
        } 
    } 
    return sumFactors;
}

int main() {
    ll t;
    cin >> t;
    while(t--) {
        ll n, q, x, y, a, u, v, ans;
        cin >> n;
        vector<ll> adj[n];
        ll countFactors[n];
        for(ll i=0; i<n-1; ++i) {
            cin >> x >> y;
            addEdge(adj, x-1, y-1);
        }
        for(ll i=0; i<n; ++i) {
            cin >> a;
            countFactors[i] = countDivisors(a);
        }
        for(int i=0; i<n; ++i) {
            cout << countFactors[i] << " ";
        }
        cout << "\n";
        cin >> q;
        for(ll i=0; i<q; ++i) {
            cin >> u >> v;
            ans = bfs(adj, n, u-1, v-1, countFactors) % 1000000007;
            cout << ans << "\n";
        }
    }
}