#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int bin2dec(char *bin) {
    int dec = 0;
    int i = 0;
    while (bin[i] != '\0') {  
        if (bin[i] == '1') {
            dec = dec * 2 + 1; 
        }
        else if (bin[i] == '0') {
            dec *= 2; 
        }
        i++;
    } 
    return dec;
}

int main(void) {
    int t;
    scanf("%d", &t);
    while(t--) {
        char *x = (char*) malloc(pow(10, 5)*sizeof(char));
        char *y = (char*) malloc(pow(10, 5)*sizeof(char));
        printf("%d\n", sizeof(x));
        scanf("%s", x);
        scanf("%s", y);

        int a = bin2dec(x);
        int b = bin2dec(y);
        int u, v;
        int count = 0;
        while (b>0) {
            u = a ^ b;
            v = a & b;
            a = u;
            b = v * 2;
            count++;
        }
        free(x);
        free(y);
        printf("%d\n", count);
    }
}