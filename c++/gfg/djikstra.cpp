#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pl;

vector<ll> djikstra(unordered_map<ll, unordered_map<ll,ll>> graph, ll V, ll src)
{
    priority_queue<pl, vector<pl>, greater<pl>> pq;
    pq.push(make_pair(0, src));
    vector<ll> dist(V, -1);

    while (!pq.empty())
    {
        pair<int,int> p = pq.top();
        pq.pop();
        if (dist[p.second-1] == -1)
        {
            dist[p.second-1] = p.first;
            for (auto v : graph[p.second])
            {
                pq.push(make_pair(p.first + v.second, v.first));
            }
        }
    }
    return dist;
}

int main()
{  
    const ll V = 5;
    vector<vector<ll>> edges = { {1,2,2}, {2,4,5}, {4,1,5}, {2,3,14}, {2,5,4}, {5,3,34}, {5,4,58} };
    unordered_map<ll,unordered_map<ll, ll>> graph;
    for (int i=1; i<=V; i++)
    {
        graph.insert(make_pair(i, unordered_map<ll,ll>()));
    }
    for (auto v : edges)
    {
        graph[v[0]][v[1]] = v[2];
        graph[v[1]][v[0]] = v[2];
    }
    vector<ll> dist = djikstra(graph, V, 1);
    for (auto i : dist)
        cout << i << " "; 
    cout << endl;
    
}