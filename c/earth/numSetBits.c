#include <stdio.h>
#include <stdlib.h>

void numSetBits(int n)
{
    int count = 0;
    while(n)
    {
        n = n & (n-1);
        ++count;
    }
    printf("%d\n", count);
}

int main(void)
{
    int n, t;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        numSetBits(n);
    }
}
