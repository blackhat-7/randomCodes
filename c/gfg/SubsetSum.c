#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int t;
	scanf("%d", &t);
	while(t--) {
	    int n;
	    scanf("%d", &n);
	    int **dp = (int **)malloc(n*sizeof(int*));
	    for(int i=0; i<n; ++i){
	        dp[i] = (int *)malloc(n*sizeof(int));
	        memset(dp[i], 0, n*sizeof(int));
	    }
        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; ++j) {
                
            }
        }
	}
	return 0;
}