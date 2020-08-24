#include <bits/stdc++.h>
#include <chrono>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, n;
    int arr[1000000];
    cin >> t;
    while (t--)
    {
        auto start = chrono::high_resolution_clock::now();
        cin >> n;
        for (int i = 0; i < n; ++i)
        {
            cin >> arr[i];
        }
        int curr_sum = arr[0], max_sum = arr[0];
        for (int i = 1; i < n; ++i)
        {
            if (curr_sum + arr[i] < arr[i])
            {
                curr_sum = arr[i];
                max_sum = (curr_sum > max_sum) ? curr_sum : max_sum;
            }
            else
            {
                curr_sum += arr[i];
                max_sum = (curr_sum > max_sum) ? curr_sum : max_sum;
            }
        }
        auto end = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsed = end - start;
        cout << max_sum << " time:" << elapsed.count() << endl;
    }
}
