#ifndef MAXFLOWGRAPH_H
#define MAXFLOWGRAPH_H
#include <vector>
#include <iostream>

class Graph {
private:
    int V;
    bool bfs_ford(int s, int t, int parent[]);

public:
    std::vector<int> *adj;
    Graph(int V) { 
        this->V = V;
        adj = new std::vector<int>[V];
        for(int i=0; i<V; ++i) {
            adj[i] = *(new std::vector<int>(V));
        }
    }
    ~Graph() { 
        delete [] adj;
    }
    void add_edge(int src, int dest, int cap);
    void remove_edge(int src, int dest);
    bool bfs(int s, int t, std::vector<int> &parent);
    int ford_fulkerson(int s, int t);
    void print_matrix();

};

#endif