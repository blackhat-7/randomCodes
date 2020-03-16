#include <bits/stdc++.h>

int main() {
    int n, t, x, y, min = std::numeric_limits<int>::max();
    std::cin >> n >> t;
    std::vector<int> v(n);
    std::vector<int> minWidthTilln(n);
    
    for (int i=0; i<n; i++) {
        std::cin >> v[i];
        if (v[i] < min) {
            min = v[i];
            minWidthTilln[i] = min;
        }
    }
    while(t--) {
        std::cin >> x >> y;
        std::cout << v[std::min_element(v.begin()+x, v.begin()+y)-v.begin()] << std::endl;
    }
}