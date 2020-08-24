#include <bits/stdc++.h>
using namespace std;
// #define ll long long

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;
    int n = s.length(), plusCount = 0, minusCount = 0;
    for(int i=0; i<n; ++i) {
        if(s[i] == '+') ++plusCount;
        else ++minusCount;
    }
    cout << abs(plusCount-minusCount) << "\n";
}