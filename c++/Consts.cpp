#include <iostream>

int main()
{
    int var = 90;
    int var2 = 80;
    const int* X = &var;
    int* const Y = &var2;
    
    // Cannot change value stored in X
    X = &var2;
    
    // Cannot change what Y points to
    *Y = 5;
    
    std::cout << *X << std::endl;
    std::cout << *Y << std::endl;

}
