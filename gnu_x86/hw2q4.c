#include <stdio.h>

int x = 2;
void foo() {
    printf("%d\n", x);
    x = 0;
    printf("%d\n", x);
}
int main()
{
    foo();
}
