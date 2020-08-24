#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void)
{
    int n, q, l, r, i,iCount, dCount;
    scanf("%d %d", &n, &q);
    int *arr = (int*) malloc(n*sizeof(int));
    for (i=0; i<n; ++i)
    {
        scanf("%d", &arr[i]);
    }
    while(q--)
    {
        iCount = 0; dCount = 0;
        scanf("%d %d", &l, &r);

        for (i=l+1; i<=r; ++i)
        {
            if (i==l+1 && arr[i]>arr[i-1])
            {
                ++iCount;
            }
        }

    }
}
