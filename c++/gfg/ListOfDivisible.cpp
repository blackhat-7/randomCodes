#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

int main()
{
    /*
    
    int n;
    std::cin >> n;
    std::vector<int> vec(n);
    for (int i=0; i<n; i++) {
        std::cin >> vec[i];
    }
    int k;
    std::cin >> k;
    
    //divisiblity
    std::vector<int> divisibles;
    std::copy_if(vec.begin(), vec.end(), std::back_inserter(divisibles),
            [k](int dividend) {return dividend % k == 0;});
    
    std::cout << "Divisibles by " << k << " :\n";
    for (auto i : divisibles) {
        std::cout << i << " ";
    }
    std::cout << std::endl;



    //power
    std::vector<int> powers;
    std::for_each(vec.begin(), vec.end(),
            [&](int x){ powers.emplace_back(std::pow(x, k)); });

    std::cout << "Powered to " << k << " :\n";
    for (auto i : powers) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    
    int n;
    std::cin >> n;
    std::vector<int> vec1(n);
    std::vector<int> vec2(n);
    for (int i=0; i<n; i++)
        std::cin >> vec1[i];
    for (int i=0; i<n; i++)
        std::cin >> vec2[i];

    //code
    std::vector<int> sum(n);
    std::transform(vec1.begin(), vec1.end(), vec2.begin(), sum.begin(), 
            [](int x, int y) { return x + y; });

    std::cout << "Sum of both :\n";
    for (auto i : sum) {
        std::cout << i << " ";
    }
    std::cout << std::endl;


    std::function<int(int)> Fib = [&Fib](int x) {
        return (x < 2) ? x : Fib(x-1) + Fib(x-2);
    };

    std::cout << Fib(12) << std::endl;
    */

    int n;
    std::cin >> n;

    std::vector<long long> fibs(n);
    
    std::function<int(int)> Fib = [&Fib](int x) {
        return (x < 2) ? x : Fib(x-1) + Fib(x-2);
    };
    int i = 0;
    while(i < n) {
        fibs[i] = Fib(i);
        i++;
    }
    for (auto i : fibs) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}
