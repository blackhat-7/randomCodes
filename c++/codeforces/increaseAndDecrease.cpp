#include <bits/stdc++.h>
using namespace std;
// #define ll long long

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; ++i) {
        cin >> arr[i];
    }
    int mid = n/2, left = -1, right = n;
    for(int i=n/2; i>=0; --i) {
        if(arr[i] != arr[mid]) {
            left = i;
            break;
        }
    }
    for(int i=n/2; i<n; ++i) {
        if(arr[i] != arr[mid]) {
            right = i;
            break;
        }
    }
    int extra = 0;
    while(left >= 0 && right < n) {
        extra = 2*arr[mid] - arr[left] - arr[right]
        if (extra > 0) {
            arr[right] = arr[mid] - arr[right];
        }
        else {
            exra = abs(axtra);
            arr[ ]
        }
    }
}