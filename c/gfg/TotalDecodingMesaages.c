#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        scanf("%d", &n);
        char s[n];
        scanf("%s", s);
        int *dp = (int *)malloc(n * sizeof(int));
        if (n<=1) {
            printf("1\n"); continue;
        }
        if (n==2) {
            char s1[2];
            strncpy(s1, &s[0], 2);
            int x = atoi(s1);
            if (x>26 && x%10==0 || x==0) {
                printf("0\n"); continue;
            }
            if (x <= 26) {
                printf("3\n"); continue;
            }
            printf("2\n"); continue;
        }
        dp[0] = 1;
        dp[1] = 2;
        for (int i = 2; i < n; ++i)
        {
            char s1[2];
            strncpy(s1, &s[i-1], 2);
            int x = atoi(s1);
            dp[i] = (x <= 26) ? dp[i - 1] + dp[i - 2] : dp[i - 1];
            if(x>26 && x%10==0 || x == 0) {
                dp[n-1] = 0; break;
            }
        }
        printf("%d\n", dp[n-1]);
    }
    return 0;
}