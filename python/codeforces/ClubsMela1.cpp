#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, q;
    cin>>n>>q;

    vector<int> maxi(n+1, -1);
    for(int i=0; i<n+1; i++) {
		maxi[i] = -1;
    }
    
    for(int i=0; i<n; i++) {
    	int a, b;
    	cin>>a>>b;
    	maxi[b] = max(maxi[a], b);
    }
    
    for(int i=0; i<n; i++) {
    	int x;
    	cin>>x;
    	cout<<maxi[x]<<endl;
    }
}