#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int t, n;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        int *scores = (int*) malloc(8*sizeof(int));
        memset(scores, 0, 8*sizeof(int));
        int p, s, sum = 0;

        for(int i=0; i<n; i++) {
            scanf("%d %d", &p, &s);
            if (p<9 && s>scores[p-1]) {
                sum -= scores[p-1];
                scores[p-1] = s;
                sum += scores[p-1];
            }
        }
        printf("%d\n", sum);
    }
}