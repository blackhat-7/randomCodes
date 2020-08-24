#include <iostream>

int main()
{
    int var = 90;
    int var2 = 80;
    const int* X = &var;
    int* const Y = &var2;

    X = &var2;

    *Y = 5;
    
    std::cout << *X << std::endl;
    std::cout << *Y << std::endl;

}
