#ifndef GRAPH_H
#define GRAPH_H
#include <vector>

class Graph {
private:
    int V;
    std::vector<std::pair<int, int>> *adj;

public:
    Graph(int V) { 
        this->V = V;
        adj = new std::vector<std::pair<int, int>>[V];
    }
    ~Graph() { 
        delete [] adj;
    }
    void addEdge(int src, int dest, int wt);
    void bfs(int src);

};

#endif

//fixed