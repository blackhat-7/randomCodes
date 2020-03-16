#include <iostream>

int main() {
    int arr[] = {5, 6, 7, 8, 9};
    int *parr = &arr[0];
    int i = 0;
    std::cout << "print" << std::endl;
    while(i != sizeof(arr)/sizeof(int)) {
        std::cout << *parr++ << std::endl;
        i++;
    }

    int value = 10;
    const int* const pValue = &value;

    std::cout << *pValue << std::endl;
    
    int value2 = 11;
    // pValue = &value2;
    // *pValue = value2;
    std::cout << *pValue << " " << sizeof(pValue) << std::endl;
}