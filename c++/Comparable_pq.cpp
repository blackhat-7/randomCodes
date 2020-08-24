#include <bits/stdc++.h>
using namespace std;

class Compare
{
public:
    bool operator() (pair<int,int> a, pair<int,int> b)
    {
        if (a.second == b.second)
            return a.first < b.first;
        return a.second - b.second;
    }
};


int main()
{
    // priority_queue<pair<int,int>, vector<pair<int,int>>, Compare> pq;
    // pq.push(make_pair(5, 2));
    // pq.push(make_pair(6, 4));
    // pq.push(make_pair(5, 4));
    // pq.push(make_pair(9, 2));
    // pq.push(make_pair(6, 1));
    // while (!pq.empty())
    // {
    //     cout << pq.top().first << " " << pq.top().second << endl;
    //     pq.pop();
    // }
    unordered_map<int,int> counts;
    vector<int> nums = {5,2,5,5,3,2,2};
    for (auto i : nums)
    {
        counts[i]++;
    }
    for (auto i = counts.begin(); i != counts.end(); i++){
        cout << i->first << " " << i->second << endl;
    }
}