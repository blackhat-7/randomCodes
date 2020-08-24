#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n;
    cin >> t;
    while(t--) {
        cin >> n;
        if(n < 3) {
            if(n==1) {
                cout << "1\n1 1\n";
            }
            else if(n==2) {
                cout << "1\n2 1 2\n";
            }
        }
        else {
            cout << 1+(n-2)/2 << "\n";
            cout << "3 1 2 3\n";
            for(int i=4; i<=n; i+=2) {
                if (i!=n) {
                    cout << "2 " << i << " " << i+1 << "\n";
                }
                else {
                    cout << "1 " << i << "\n"; 
                }
            }
        }
    }
}