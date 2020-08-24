#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>



using namespace std;

typedef long long ll;
typedef pair<ll,ll> pl;

void bfs(unordered_map<ll,vector<pl>> graph, ll src, ll numVertices) 
{
    queue<ll> q;
    q.emplace(src);
    bool visited[numVertices];
    fill(visited, visited + numVertices, false); 
    visited[src] = true;
    while (!q.empty())
    {
        ll u = q.front();
        cout << u << " ";
        q.pop();
        for (auto edge : graph[u])
        {
            if (!visited[edge.first])
            {
                q.emplace(edge.first);
                visited[edge.first] = true;
            }
        }
    }
    cout << "\n";
}


void dfs(unordered_map<ll,vector<pl>> graph, ll u, bool visited[], ll numVertices)
{
    cout << u << " ";
    visited[u] = true;
    for (auto v : graph[u])
    {
        if (!visited[v.first])
            dfs(graph, v.first, visited, numVertices);
    }
}





int main()
{
    ll numVertices = 4;
    vector<vector<ll>> edges = {{0,1,6}, {2,0,5}, {2,1,4}, {1,2,7}, {3,2,10}};

    unordered_map<ll,vector<pl>> graph;
    
    for (int i=0; i<numVertices; i++)
        graph.insert(make_pair(i, vector<pl>()));
    for (auto e : edges)
    {
        graph[e[0]].push_back(make_pair(e[1], e[2]));
        graph[e[1]].push_back(make_pair(e[0], e[2]));
    }   
    cout << "BFS: \n";
    bfs(graph, 0, numVertices);
    cout << "DFS: \n";
    bool visited[numVertices];
    dfs(graph, 0, visited, numVertices);
    cout << endl;
}
