#include <stdio.h>

int main(void) {
    int i = 90;
    float f = 3;
    printf("f = %f i = %d\n", f);
    printf("f = %f\n", f, i);
    printf("i = %d f = %f\n", f, i);

    int x;
    {
        x = 0;
    }
    printf("%d\n", x);
}