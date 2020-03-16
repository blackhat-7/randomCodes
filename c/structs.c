#include <stdio.h>

struct Point {
    int x, y;
};

int main(void) {
    struct Point p1 = {1, 2};
    struct Point *pp1 = &p1;
    printf("p1.x : %d\n", p1.x);
    printf("pp1->x : %d", pp1->x);
}