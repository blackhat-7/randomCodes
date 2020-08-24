#include <stdio.h>
#include <stdlib.h>

struct box
{
    int length, breadth, height;
};
typedef struct box box;

int main(void)
{
    int n;
    scanf("%d", &n);
    box *boxArr = (box*) malloc(n * sizeof(box*));

    scanf("%d", &n);
    for (int i=0; i<n; ++i)
    {
        scanf("%d %d %d", &(boxArr[i]->length), boxArr[i]->breadth, )
    }
    i
    
}
