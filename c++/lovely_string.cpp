#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int t;
    string name;
    cin >> t;
    while (t--)
    {
        unordered_map<char, int> l_vowels({{'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}});
        unordered_map<char, int> u_vowels({{'A', 0}, {'E', 0}, {'I', 0}, {'O', 0}, {'U', 0}});
        cin >> name;
        for (char c : name)
        {
            if (l_vowels.find(c) != l_vowels.end())
            {
                l_vowels[c]++;
            }
            if (u_vowels.find(c) != l_vowels.end())
            {
                u_vowels[c]++;
            }
        }
        bool lovely = true;
        for (auto m : l_vowels)
        {
            if (m.second == 0)
            {
                lovely = false;
                break;
            }
        }
        if (lovely)
        {
            cout << "lovely string\n";
            continue;
        }
        lovely = true;
        for (auto m : u_vowels)
        {
            if (m.second == 0)
            {
                lovely = false;
                break;
            }
        }
        if (lovely)
        {
            cout << "lovely string\n";
            continue;
        }
        cout << "ugly string\n";
    }
}