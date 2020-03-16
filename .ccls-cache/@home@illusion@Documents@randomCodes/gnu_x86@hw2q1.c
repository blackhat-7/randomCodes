int bar(int a, int b, int c, int d) {
    int x, y, z, w;
    x = a, y = b, z = c, w = d;
    return x + y + z + w;
}

int foo () {
    int a, b, c, d, e, f;
    a = 0, b = 1, c = 2, d = 3;
    e = 5, f = 6;
    bar(b, c, d, f);
    return a + b + c;
}

