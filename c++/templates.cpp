#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

template<typename T>
T Max(T stuff1, T stuff2) {
    return (stuff1 > stuff2) ? stuff1 : stuff2;
}



template<class T>
class GenericList
{
    public:
        std::vector<T> myList;
        GenericList() {}

        void push_back(T item) {
            myList.push_back(item);
        }

        void pop_back() {
            myList.pop_back();
        }
};













int main()
{
    /*
       std::cout << Max(10, 3) << std::endl;
       std::cout << Max(1.234, 234.3) << std::endl;
       std::cout << Max(1000000000000, 3000000000000) << std::endl;
       std::cout << Max('A', 'H') << std::endl;
       std::cout << Max("asdas", "jhkhj") << std::endl;
       std::cout << Max(true, false) << std::endl;
       */

    GenericList<std::pair<int,char>> l;
    l.push_back(std::make_pair(5, '5'));
    l.push_back(std::make_pair(4, '4'));
    l.push_back(std::make_pair(1, '1'));
    l.push_back(std::make_pair(9, '9'));
    l.pop_back();

}
