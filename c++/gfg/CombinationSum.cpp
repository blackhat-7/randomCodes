#include <iostream>
#include <vector>

using namespace std;


vector<vector<int>> solve(int n) {
    if (n == 0 || n == 1) {
        vector<vector<int>> v2d(1);
        // v2d[0].emplace_back(n);
        return v2d;
    }
    vector<vector<int>> res;
    for (int i=1; i<n/2+1; i++) {
        vector<vector<int>> v2d1 = solve(i);
        vector<vector<int>> v2d2 = solve(n-i);
        for (auto v1 : v2d1) {
            for (auto v2 : v2d2) {
                v1.insert(v1.end(), v2.begin(), v2.end());
                res.insert(res.end(), v1.begin(), v1.end());
            }
        }
    }
    return res;
}

int main()
{
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<vector<int>> v2d = solve(n);
        for (vector<int> v : v2d) {
            for (int i : v) {
                cout << i << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}