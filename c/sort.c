#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *selectionSort(int *arr, int n);
int *insertionSort(int *arr, int n);
int *bubbleSort(int *arr, int n);
int *mergeSort(int *arr, int l, int r);
void merge(int *arr, int l, int m, int r);
void printArr(int *arr, int n);
int *deepCopy(int *arr, int n);

typedef enum bool {
    true,
    false
} bool;

int main(void) {
    bool boolean = true;
    
    int n, *arr, *sortedArr;
    scanf("%d", &n);
    arr = malloc(n*sizeof(int));
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Merge : ");
    sortedArr = mergeSort(deepCopy(arr, n), 0, n-1);
    printArr(sortedArr, n);

    free(sortedArr);

    printf("Selection : ");
    sortedArr = selectionSort(arr, n);
    printArr(sortedArr, n);

    free(sortedArr);
    
    printf("Insertion : ");
    sortedArr = insertionSort(arr, n);
    printArr(sortedArr, n);

    free(sortedArr);

    printf("Bubble : ");
    sortedArr = bubbleSort(arr, n);
    printArr(sortedArr, n);

    free(sortedArr);
    free(arr);
}



int *mergeSort(int *arr, int l, int r) {
    if (l<r) {
        int m = (l+r)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
    return arr;
}

void merge(int *arr, int l, int m, int r) {
    int n1 = m - l;
    int n2 = r - m - 1;
    int *left = malloc(n1 * sizeof(int));
    int *right = malloc(n2 * sizeof(int));

    for(int i=0; i<=n1; ++i) {
        left[i] = arr[i+l];
    }
    for(int i=0; i<=n2; ++i) {
        right[i] = arr[i+m+1];
    }
    int i=l, j=0, k=0;
    while (j <= n1 && k <= n2) {
        if (left[j] <= right[k]) {
            arr[i] = left[j];
            j++;
        }
        else {
            arr[i] = right[k];
            k++;
        }
        i++;
    }
    while (j <= n1) {
        arr[i] = left[j];
        i++; j++;
    }
    while (k <= n2) {
        arr[i] = right[k];
        i++; k++;
    }
}

int *insertionSort(int *arr, int n) {
    int *copy = deepCopy(arr, n);
    for (int i=1; i<n; ++i) {
        int j = i-1;
        while (j>=0 && copy[j]>copy[j+1]) {
            int temp = copy[j];
            copy[j] = copy[j+1];
            copy[j+1] = temp;
            --j;
        }
    }
    return copy;
}

int *selectionSort(int *arr, int n) {
    int *copy = deepCopy(arr, n);
    int min, minIndex;
    for (int i=0; i<n-1; ++i) {
        min = copy[i];
        minIndex = i;
        for (int j=i; j<n; ++j) {
            if (copy[j] < min) {
                min = copy[j];
                minIndex = j;
            }
        }
        int temp = copy[i];
        copy[i] = min;
        copy[minIndex] = temp;
    }
    return copy;
}

int *bubbleSort(int *arr, int n) {
    int *copy = deepCopy(arr, n);
    for(int i=1; i<n; i++) {
        for(int j=1; j<n; j++) {
            if (copy[j] < copy[j-1]) {
                int temp = copy[j];
                copy[j] = copy[j-1];
                copy[j-1] = temp;
            }
        }
    }
    return copy;
}

void printArr(int *arr, int n) {
    for (int i=0; i<n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int *deepCopy(int *arr, int n) {
    int *copy = malloc(n * sizeof(int));
    for(int i=0; i<n; ++i) {
        copy[i] = arr[i];
    }
    return copy;
}
