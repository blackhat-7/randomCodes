#include <stdio.h>

union Data {
    int x;
    float y;
    char str[50];
};

int main(void) {
    union Data d1;
    printf("Total memory allocated : %d\n", sizeof(d1));
    printf("memory allocated to x : %d\n", sizeof(d1.x));
    printf("memory allocated to y : %d\n", sizeof(d1.y));
    printf("memory allocated to str : %d\n", sizeof(d1.str));

    d1.x = 4;
    printf("location of x : %d\n", &d1.x);
    d1.y = 4.123;
    printf("location of y : %d\n", &d1.y);
    d1.str[0] = 'b';
    d1.str[1] = 'c';
    printf("location of str : %d\n", &d1.x);
}