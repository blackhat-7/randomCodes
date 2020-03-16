#include <stdio.h>
#include <math.h>
#include <stdlib.h>

typedef unsigned long long ulli;

int main(void)
{
        int t;
        ulli n, s, a, b, c, d, e, verdict;
        scanf("%d", &t);
        while(t--)
        {
                scanf("%llu %llu", &n, &a);
                s = 2*pow(10, n) + a;
                
                printf("%llu\n", s);
                fflush(stdout);
                
                scanf("%llu", &b);
                c = pow(10, n) - b;

                printf("%llu\n", c);
                fflush(stdout);
                
                scanf("%llu", &d);
                e = pow(10, n)-d;

                printf("%llu\n", e);
                fflush(stdout);
                
                ulli ans = a+b+c+d+e;
                printf("%llu\n", ans);
                printf("%llu\n", s);
                fflush(stdout);
                
                scanf("%llu", &verdict);
                if (verdict == -1)
                {
                        exit(0);
                }
        }
}
