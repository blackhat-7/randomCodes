#include <bits/stdc++.h>

int main() {
    int n, d;
    std::cin >> n >> d;

    std::vector<int> v(n);

    for (int i=0; i<n; i++) {
        std::cin >> v[i];
    }  
    int counter = 0;

    for (int i=0; i<n; i++) {
        if (std::binary_search(v.begin(), v.end(), v[i]+d) && std::binary_search(v.begin(), v.end(), v[i]+d)) {
            counter++;
        }
    }
    std::cout << counter;
}
