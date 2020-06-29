#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int minimum(int a, int b) { return a < b ? a : b; }
int maximum(int a, int b) { return a > b ? a : b; }


int main() {
	int t, n;
	scanf("%d", &t);
	while(t--) {
	    scanf("%d", &n);
	    int *arr = malloc(n * sizeof(int));
	    for(int i=0; i<n; ++i) {
	        scanf("%d", &arr[i]);
	    }
		int *minimumArr = malloc(n * sizeof(int));
		minimumArr[0] = arr[0];
		int *maximumArr = malloc(n * sizeof(int));
		maximumArr[n-1] = arr[n-1];
	    for(int i=0; i<n; ++i) {
	        minimumArr[i] = minimum(arr[i], minimumArr[i-1]);
			maximumArr[n-2-i] = maximum(arr[n-2-i], maximumArr[n-1-i]);
	    }
		int l = 0;
		int r = 0;
		int maximumDiff = -1;
		while(l<=r) {
			if (minimumArr[l] < maximumArr[r]) {
				maximumDiff = maximum(maximumDiff, r-l);
				++r;
			}
			else 
				++l;
		}
		printf("%d", maximumDiff);
		free(arr);
		free(minimumArr);
		free(maximumArr);
	}
	return 0;
}