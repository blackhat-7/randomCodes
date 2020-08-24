#include <stdio.h>
#include <stdlib.h>

int stringLen(char *s)
{
    int n = 0;
    while (*s != '\0')
    {
         ++n; ++s;
    }
    return n;
}

int main(void)
{
    char *s = "hello world";
    printf("length of string : %d\n", stringLen(s));
    int n;
    int arr[n];
    return 0;
}
