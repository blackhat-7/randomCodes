#include "MaxFlowGraph.h"
#include <queue>
#include <string.h>
#include <limits.h>

void Graph::print_matrix()
{
    for (int i = 0; i < V; ++i)
    {
        for (int j = 0; j < V; ++j)
        {
            std::cout << adj[i][j] << " ";
        }
        std::cout << "\n";
    }
}

void Graph::add_edge(int s, int d, int c)
{
    adj[s][d] = c;
}

void Graph::remove_edge(int s, int d)
{
    adj[s][d] = 0;
    adj[d][s] = 0;
}

bool Graph::bfs(int s, int t, std::vector<int> &parent)
{
    std::vector<bool> visited(V, false);
    std::queue<int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        if (u == t)
        {
            break;
        }
        for (int i = 0; i < V; ++i)
        {
            if (adj[u][i] > 0 && !visited[i])
            {
                visited[i] = true;
                parent[i] = u;
                q.push(i);
            }
        }
    }
    return visited[t] == true;
}

int Graph::ford_fulkerson(int s, int t)
{
    Graph rg(V);
    for (int i = 0; i < V; ++i)
    {
        for (int j = 0; j < V; ++j)
        {
            rg.add_edge(i, j, adj[i][j]);
        }
    }
    std::vector<int> parent(V, -1);
    int max_flow = 0;
    while (rg.bfs(s, t, parent))
    {
        int path_flow = INT_MAX;
        for (int i = t; i != s; i = parent[i])
        {
            int u = parent[i];
            path_flow = std::min(path_flow, rg.adj[u][i]);
        }

        for (int i = t; i != s; i = parent[i])
        {
            rg.adj[parent[i]][i] -= path_flow;
            rg.adj[i][parent[i]] += path_flow;
        }

        max_flow += path_flow;
    }
    return max_flow;
}

int main()
{
    Graph g(6);
    g.add_edge(0, 1, 16);
    g.add_edge(0, 2, 13);
    g.add_edge(1, 2, 10);
    g.add_edge(1, 3, 12);
    g.add_edge(2, 1, 4);
    g.add_edge(2, 4, 14);
    g.add_edge(3, 2, 9);
    g.add_edge(3, 5, 20);
    g.add_edge(4, 3, 7);
    g.add_edge(4, 5, 4);
    std::cout << g.ford_fulkerson(0, 5) << "\n";
}