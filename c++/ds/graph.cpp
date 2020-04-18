#include <iostream>
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

int main() {
    Graph g(4);
    g.addEdge(0, 1, 2);
    g.addEdge(1, 2, 5);
    g.addEdge(0, 3, 4);
    g.bfs(0);
}