int bar(int *x, int *y) {
    *x = 0;
    *y = 1;
}

void foo (int a, int b) {
    bar(&a, &b);
}
