#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
typedef long long ll;

// ll arr[10000000];

ll fun(string s, ll n, ll k, char c)
{
    ll left_pointer = 0;
    ll right_pointer = -1;
    ll curr_changes = 0;
    ll max_len = 0;
    for (int i=0; i<n; i++)
    {
        right_pointer++;
        if (s[i] == c) curr_changes++;
        while (curr_changes > k)
        {
            if (s[left_pointer] == c) curr_changes--;
            left_pointer++;
        }
        max_len = max(max_len, right_pointer - left_pointer + 1);
    }
    return max_len;
}

void solve()
{
    ll n, k;
    string s;
    cin >> n >> k;
    cin >> s;
    ll left = 0, right = 0;
    ll maxA = fun(s, n, k, 'a');
    ll maxB = fun(s, n, k, 'b');
    cout << max(maxA, maxB) << endl;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t = 1;
    // cin >> t;

    while (t--) {
        solve();
    }
}
