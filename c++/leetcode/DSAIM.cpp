#include <bits/stdc++.h>
using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s, result;
    cin >> s;
    int n = s.length();
    for (int i=0; i<n; ++i)
    {
        if (i+2<n && s[i+2]!='#')
        {
            result+=char(96+(int)s[i]);
        }
        else
        {
            int x = (int)(s[i]+s[i+1]);
            result += char(96+x);
        }
        cout << result << endl;
    }
}