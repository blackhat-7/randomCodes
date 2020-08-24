#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        stack<char> s;
        bool balanced = true;
        string str;
        cin >> str;
        int l = str.length();
        for (int i = 0; i < l; ++i)
        {
            if (str[i] == '{' || str[i] == '(' || str[i] == '[')
            {
                s.push(str[i]);
            }
            else if (!s.empty() && (str[i] == '}' && s.top() == '{' || str[i] == ')' && s.top() == '(' || str[i] == ']' && s.top() == '['))
            {
                s.pop();
            }
            else
            {
                balanced = false;
                break;
            }
        }
        if (!s.empty())
            balanced = false;
        if (balanced)
            cout << "balanced" << endl;
        else
            cout << "not balanced" << endl;
    }
}
