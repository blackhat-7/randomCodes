#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int t, n;
    scanf("%d", &t);
    while(t--) {
        
        scanf("%d", &n);
        int numOf0s = 0;
        int numOf2s = 0;

        int x;
        for (int i=0; i<n; i++) {
            scanf("%d", &x);
            if (x==0) numOf0s++;
            else if (x==2) numOf2s++;
        }

        long int pairs0 = numOf0s*(numOf0s-1)/2;
        long int pairs2 = numOf2s*(numOf2s-1)/2;

        printf("%ld\n", pairs0+pairs2);
    }
}
/*

x + y = x * y
y = x * (y - 1)
x = y/(y-1)
y = x*(y-1)

*/