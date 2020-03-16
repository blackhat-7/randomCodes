#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, *arr;
    scanf("%d", &n);
    arr = malloc(n * sizeof(int));

    for(int i=0; i<n; i++) {
        scanf("%d", arr+i);
    }

    for(int i=0; i<n; i++) {
        printf("%d ", *(arr+i));
    }
    printf("\n");

    int x;
    scanf("%d", &x);
    arr = realloc(arr, n+1);
    *(arr+n) = x;

    for(int i=0; i<n+1; i++) {
        printf("%d ", *(arr+i));
    }
    printf("\n");
    
}
