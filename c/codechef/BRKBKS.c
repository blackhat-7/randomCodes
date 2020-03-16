#include <stdio.h>

int main(void)
{
    int t, s, w1, w2, w3;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d %d %d %d", &s, &w1, &w2, &w3);
        int hits = 1, n = s;
        n -= w1;
        if (n >= w2)
        {
            n -= w2;
            if (n < w3)
            {
                ++hits; 
            }
        }
        else
        {
            ++hits;
            n = s-w2;
            if (n < w3)
            {
                ++hits;
            }
        }
        printf("%d\n", hits);
    }
}
