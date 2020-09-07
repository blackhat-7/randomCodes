#include <iostream>

using namespace std;


void merge(int arr[], int n, int low, int mid, int high) {
    int temp_arr[high-low+1];
    int i = low, j = mid+1, k = 0;
    while (i <= mid && j <= high)
    {
        if (arr[i] < arr[j]) {
            temp_arr[k] = arr[i];
            i++;
        } else {
            temp_arr[k] = arr[j];
            j++;
        }
        k++;
    }
    while (i <= mid)
    {
        temp_arr[k] = arr[i];
        i++; k++;
    }
    while (j <= mid)
    {
        temp_arr[k] = arr[j];
        j++; k++;
    }
    for (int i=low; i<=high; i++)
    {
        arr[i] = temp_arr[i-low];
    }
}

void merge_sort(int arr[], int n, int low, int high)
{
    if (low <= high)
    {
        if (low == high)
            return;
        int mid = low + (high-low)/2;
        merge_sort(arr, n, low, mid);
        merge_sort(arr, n, mid+1, high);
        merge(arr, n, low, mid, high);
        return;
    }

}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i=0; i<n; i++) cin >> arr[i];
    merge_sort(arr, n, 0, n-1);
    for (int i=0; i<n; i++) cout << arr[i] << " ";
    cout << "\n";
}
