#include <bits/stdc++.h>
using namespace std;

int factorial(int n)
{
    if (n==1)
    {
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}

void subset(int k, vector<int> v, int n)
{
    if (k==n+1)
    {
        for(int i=0; i<v.size(); i++)
        {
            cout<<v[i]<<" ";
        }
        cout<<"\n";
    }
    else
    {
        v.push_back(k);
        subset(k+1, v, n);
        v.pop_back();
        subset(k+1, v, n);
    }
}

void permuation(vector<int> v, vector<int> p)
{
    if (p.size()==v.size())
    {
        for(int i=0; i<p.size(); i++)
        {
            cout<<p[i]<<"\n";
        }
    }

}

int main()
{
    vector<int> v;
    vector<int> p;
}
