#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, *arr = new int[101], x, ans;
    memset(arr, 0, 100 * sizeof(int));
    cin >> n;
    for (int i=0; i<n; ++i)
    {
        cin >> x;
        arr[x] += 1;
    }
    for (int i=0; i<101; ++i)
    {
        if (arr[i] == 1)
        {
            cout << i << endl;
        }
    }
    return 0;
}
