#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "queue.h"

struct AdjListNode
{
    int dest;
    struct AdjListNode *next;
};

struct AdjList
{
    struct AdjListNode *head; 
};

struct Graph
{
    int V;
    struct AdjList *array;
};

struct AdjListNode *newNode(int dest)
{
    struct AdjListNode *new_node = (struct AdjListNode *)malloc(sizeof(struct AdjListNode));
    new_node->dest = dest;
    new_node->next = NULL;
    return new_node;
}

struct Graph *createGraph(int V)
{
    struct Graph *graph = (struct graph *)malloc(V * sizeof(graph));
    graph->V = V;
    graph->array = (struct AdjList *)malloc(V * sizeof(struct AdjList));
    for (int i = 0; i < V; i++)
    {
        graph->array[i].head = NULL;
    }
    return graph;
}

void addEdge(struct Graph *graph, int src, int dest)
{
    struct AdjListNode *new_node = newNode(dest);
    new_node->next = graph->array[src].head;
    graph->array[src].head = new_node;

    new_node = newNode(src);
    new_node->next = graph->array[dest].head;
    graph->array[dest].head = new_node;
}

void printGraph(struct Graph *graph)
{
    for (int i = 0; i < graph->V; ++i)
    {
        printf("%d", i);
        struct AdjListNode *pCrawl = graph->array[i].head;
        while (pCrawl)
        {
            printf(" -> %d", pCrawl->dest);
            pCrawl = pCrawl->next;
        }
        printf("\n");
        
    }
}

void bfs(struct Graph *graph, int src)
{
    int *visited = (int *)malloc(graph->V * sizeof(int));
    memset(visited, 0, graph->V * sizeof(int));
    Queue *q = createQueue(graph->V);

    visited[src] = 1;
    enqueue(q, src);

    while (!isEmpty(q))
    {
        printf("%d ", front(q));
        int s = dequeue(q);
        struct AdjListNode *pCrawl = graph->array[s].head;
        while (pCrawl)
        {
            visited[pCrawl->dest] = 1;
            enqueue(q, pCrawl->dest);
        }
    }
}

int main(void)
{
    int V = 5;
    struct Graph *graph = createGraph(V);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);
    // printGraph(graph);
    bfs(graph, 0);
}
