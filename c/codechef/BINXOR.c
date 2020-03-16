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

char *xor(char *bin1, char *bin2, int n) {
    char *result = (char*) malloc(n*sizeof(char));
    for (int i=0; i<n; i++) {
        if (bin1[i]==bin2[i]) {
            result[i] = '0';
        }
        else {
            result[i] = '1';
        }
    }
    return result;
}

int main(void) {
    int t, n;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        char *bin1 = (char*) malloc(n*sizeof(char));
        char *bin2 = (char*) malloc(n*sizeof(char));
        scanf("%s", bin1);
        scanf("%s", bin2);

        for (int i=0; i<n; i+=)
    }
}