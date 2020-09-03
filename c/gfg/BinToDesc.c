#include <stdio.h>
#include <math.h>

void binToDec(char* bin, int bits) {
	int len = 0;
    for (int i=0; i<bin[i] != '\0'; i++) {
		len++;
    }
	int num = 0;
	for (int i=0; bin[i] != '\0'; i++ ) {
		if (bin[i] == '1') {
			num += (int) pow(2, len-1);
		}
		len--;
	}
	printf("%d\n", num);
}

int main(void) {
	int t;
	scanf("%d", &t);
	while (t--) {
	    int bits = 16;
	    char *bin;
	    scanf("%s", bin);
	    binToDec(bin, bits);
	}
	return 0;
}
