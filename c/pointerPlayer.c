#include <stdio.h>
#include <stdlib.h>
// int *modiyArray(int *arr)
// {
// 
// }

int main(void)
{
    int val = 10;
    int *pVal = &val;
    int **ppVal = &pVal;
    printf("%d\n", val);
    int *arr = (int*) malloc(5 * sizeof(int));

    int i = 0;
    while (*arr != '\0')
    {
        printf("%d ", *arr);
        ++arr;
    }
    printf("\n");
    // modiyArray(arr);
    
}
