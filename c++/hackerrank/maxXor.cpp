#include <bits/stdc++.h>

using namespace std;

int main()
{
    int l, h, max = 0;
    cin >> l >> h;
    
    for (int i=l; i<=h; ++i)
    {
        for (int j=i; j<=h; ++j)
        {
            max = (i^j > max) ? i^j : max;
        }
    }
}
