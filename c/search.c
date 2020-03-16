#include <stdio.h>
#include <stdlib.h>

int linearSearch(int *arr, int n, int key);
int binarySearch(int *arr, int n, int key);

int main(void) {

    int n, *arr, key;
    scanf("%d", &n);
    arr = malloc(n*sizeof(int));
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("query?");
    scanf("%d", &key);
    printf("%d\n", binarySearch(arr, n, key));
    printf("%d\n", linearSearch(arr, n, key));

}

int binarySearch(int *arr, int n, int key) {
    int left = 0;
    int right = n-1;
    int mid;
    
    while(left<=right) {
        mid = left + (right-left)/2;
        
        if (key > arr[mid]) {
            left = mid+1;
        }
        else if (key < arr[mid]) {
            right = mid;
        }
        else {
            return mid;
        }
    }
    return -1;
}

int linearSearch(int *arr, int n, int key) {
    for (int i=0; i<n; ++i) {
        if (arr[i]==key) {
            return i;
        }
    }
    return -1;
}