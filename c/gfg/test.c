#include <stdio.h>
#include <stdlib.h>

int main() {
	int t, n;
	scanf("%d", &t);
	while(t--) {
	    scanf("%d", &n);
	    int *arr = malloc(n * sizeof(int));
	    for(int i=0; i<n; ++i) {
	        scanf("%d", &arr[i]);
	    }
	    for(int i=0; i<n; ++i) {
	        printf("%d\n", arr[i]);
	    }
		free(arr);
	}
	return 0;
}