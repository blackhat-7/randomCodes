#include <bits/stdc++.h>
using namespace std;

int findMax(int n, int m, int *city)
{
    int j = 0, count = 0;
    int maxDist = 0;
    for (int i=0; i<n; ++i)
    {
        if (city[i]==1)
        {
            if (j==0)
            {
                maxDist = count;
                count = 0;
                ++j;
            }
            else
            {
                ++count;
                maxDist = (count/2 > maxDist) ? count/2 : maxDist;
                count = 0;
                ++j;
            }
        }
        else
        {
            ++count;
            if (i==n-1)
            {
                maxDist = (count > maxDist) ? count : maxDist;
            }
        }
    }
    return maxDist;
}

int main() {
    int n, m, *city, x;
    cin >> n >> m;
    city = new int[n];
    memset(city, 0, n * sizeof(int));
    for (int i=0; i<m; ++i)
    {
        cin >> x;
        city[x] = 1;
    }
    int result = findMax(n, m, city);
    cout << result << endl;
}
