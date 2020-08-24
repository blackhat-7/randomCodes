#include <iostream>
#include <memory>


class Entity
{
    public:
        Entity() { 
            std::cout << "Entity created!\n"; }

        ~Entity() { std::cout << "Entity destroyed!\n"; }
};



int main()
{
    /*
       int numOfNums;
       std::cin >> numOfNums;
       std::unique_ptr<int[]> pNums(new int[numOfNums]);

       for (int i=0; i<numOfNums; i++) {
       std::cin >> pNums[i];
       }
       for (int i=0; i<numOfNums; i++) {
       std::cout << pNums[i] << " ";
       }
       std::cout << "\n";
       */
    
    std::cout << "Scope Enter1\n";
    {    
        std::shared_ptr<Entity> p_entity1;
        std::cout << "Scope Enter2\n";
        {
            std::shared_ptr<Entity> p_entity2 = std::make_shared<Entity>();
            p_entity1 = p_entity2;
        }   
        std::cout << "Scope Exit2\n";
    }
    std::cout << "Scope Exit1\n";
}
