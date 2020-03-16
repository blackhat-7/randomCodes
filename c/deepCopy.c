#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int vals[10];
} testType;

typedef struct
{
    int arr[10];
    testType ttval;
    int val;
} test;


void deepCopy(test *original, test *deep)
{
    *deep->arr = *original->arr;
    deep->ttval = original->ttval;
    deep->val = original->val;
}

int main(void)
{
    test *original = (test*) malloc(sizeof(test));
    const int temp[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; 
    memcpy(original->arr, temp, sizeof(temp));
    memcpy(original->ttval.vals, temp, sizeof(temp)); 
    original->val = 2;

    test *shallow = original;
    shallow->val = 3;
    printf("%d %d\n", original->val, shallow->val);

    test *deep = (test*) malloc(sizeof(test));
    *deep = *original;
    deep->val = 4;
    deep->arr[0] = 3;
    deep->ttval.vals[0] = 6;
    printf("%d %d\n", original->val, deep->val);
    printf("%d %d\n", original->arr[0], deep->arr[0]);
    printf("%d %d\n", original->ttval.vals[0], deep->ttval.vals[0]);
    return 0;
}
