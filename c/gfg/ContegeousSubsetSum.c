#include <stdio.h>
#include <stdlib.h>

int main() {
	int t;
	scanf("%d", &t);
    while(t--) {
        int n, s;
        scanf("%d %d", &n, &s);
        int *arr = (int*)malloc(n*sizeof(int));
        for(int i=0; i<n; ++i) {
            scanf("%d", &arr[i]);
        }
        int *sumArr = (int*)malloc((n+1)*sizeof(int));
        sumArr[0] = 0;
        sumArr[1] = arr[0];
        for(int i=2; i<n+1; ++i)
            sumArr[i] = sumArr[i-1] + arr[i-1];
        
        
        int i = 1, j = 1, found = 0;
        while(i < n+1 && j < n+1) {
            if(sumArr[j] - sumArr[i-1] == s) {
                found = 1;
                break;
            }
            else if(sumArr[j] - sumArr[i-1] > s) ++i;
            else ++j;
        }
        if(found)
            printf("%d %d\n", i, j);
        else
            printf("-1\n");
    }
	return 0;
}