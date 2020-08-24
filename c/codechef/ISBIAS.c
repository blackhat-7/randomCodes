#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int n, q, l, r;
    scanf("%d %d", &n, &q);
    int *arr = (int *)malloc(n * sizeof(int));
    int *iArr = (int *)malloc(n * sizeof(int));
    int *dArr = (int *)malloc(n * sizeof(int));
    iArr[0] = 0;
    dArr[0] = 0;

    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &arr[i]);
    }

    int iCount = 0, dCount = 0;
    // for (int i = 1; i < n; ++i)
    // {
    //     if (arr[i - 1] < arr[i] && (i == n-1 || arr[i + 1] < arr[i]))
    //     {
    //         ++iCount;
    //         printf("iCount %d\n", i);
    //     }
    //     else if (arr[i - 1] > arr[i] && (i == n-1 || arr[i + 1] > arr[i]))
    //     {
    //         ++dCount;
    //         printf("dCount %d\n", i);
    //     }
    //     iArr[i] = iCount;
    //     dArr[i] = dCount;
    // }

    int flag = 0;
    for (int i = 1; i < n; ++i)
    {
        if (arr[i] > arr[i - 1])
        {
            if (flag != 1)
            {
                ++iCount;
                printf("iCount %d\n", i);
            }
            flag = 1;
        }
        else if (arr[i] < arr[i - 1])
        {
            if (flag != -1)
            {
                ++dCount;
                printf("dCount %d\n", i);
            }
            flag = -1;
        }
        else
        {
            flag = 0;
        }

        iArr[i] = iCount;
        dArr[i] = dCount;
    }

    while (q--)
    {
        scanf("%d %d", &l, &r);
        iCount = iArr[r - 1] - iArr[l];
        dCount = dArr[r - 1] - dArr[l];
        if ((l==r-1 && arr[r-1]>arr[l-1]) || (l!=r-1 && arr[l]>arr[l-1]))
        {
            ++iCount;
        }
        if ((l==r-1 && arr[r-1]<arr[l-1]) || (l!=r-1 && arr[l]<arr[l-1]))
        {
            ++dCount;
        }
        printf("%d %d\n", iCount, dCount);
        if (iCount == dCount)
            printf("YES\n");
        else
            printf("NO\n");
    }
}

