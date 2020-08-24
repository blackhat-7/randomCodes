#include <iostream>
#include <string.h>
#include <queue>
#include "graph.h"

void Graph::addEdge(int src, int dest, int wt) {
    adj[src].push_back(std::make_pair(dest, wt));
    adj[dest].push_back(std::make_pair(src, wt));
}

void Graph::bfs(int src) {
    int visited[V];
    for(int i=0; i<V; ++i) {
        visited[i] = false;
    }
    visited[src] = true;
    std::queue<int> q;
    q.push(src);
    while(!q.empty()) {
        src = q.front();
        std::cout << src << " ";
        q.pop();
        for(auto i = adj[src].begin(); i != adj[src].end(); ++i) {
            if(!visited[i->first]) {
                q.push(i->first);
                visited[i->first] = true;
            }
        }
    }
    std::cout << "\n";
}

bool Graph::bfs_ford(int s, int t, int parent[]) {
    int visited[V];
    memset(visited, 0, sizeof(visited));
    visited[s] = true;
    std::queue<int> q;
    q.push(s);
    parent[s] = -1;
    while(!q.empty()) {
        s = q.front();
        q.pop();
        for(auto i = adj[s].begin(); i != adj[s].end(); ++i) {
            if(!visited[i->first] && i->second > 0) {
                q.push(i->first);
                visited[i->first] = true;
                parent[i->first] = s;
            }
        }
    }
    return visited[t];
}

void Graph::fordFulkerson(int s, int t) {
    int r_graph[V][V];
    for(int i = 0; i<V; ++i) {
        for(auto j = adj[i].begin(); j!=adj[i].end(); ++j) {
            r_graph.addEdge(i, j->first, j->second);
        }
    }
    r_graph.bfs(0);
    int parent[V];
    int max_flow = 0;
    int count = 0;
    while(bfs_ford(s, t, parent)) {
        int u, path_flow = INT32_MAX;
        for(int i=0; i<V; ++i) {
            u = parent[i];
            path_flow = min(path_flow, adj[u])
        }
    }
    std::cout << count << "\n";
}

int main() {
    Graph g(4);
    g.addEdge(0, 1, 2);
    g.addEdge(1, 2, 5);
    g.addEdge(0, 3, 4);
    g.bfs(0);
    g.fordFulkerson(0, 2);
}