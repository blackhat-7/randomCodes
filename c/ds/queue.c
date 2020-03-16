#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "queue.h"


struct Queue {
    int front, rear, size;
    unsigned capacity;
    int *array;
};

Queue *createQueue(int cap) {
    Queue *queue = (Queue*) malloc(sizeof(Queue));
    queue->front = queue->rear = queue->size = 0;
    queue->capacity = cap;
    queue->array = (int*) malloc(cap * sizeof(int));
    return queue;
}

int isFull(Queue *q) {
    return q->size == q->capacity;
}

int isEmpty(Queue *q) {
    return q->size == 0;
}

void enqueue(Queue *q, int data) {
    if (isFull(q))
        return;
    ++(q->rear);
    q->array[q->rear] = data;
    ++(q->size);
}

int dequeue(Queue *q) {
    if (isEmpty(q))
        return INT_MIN;
    int data = q->array[q->front];
    ++(q->front);
    --(q->size);
    return data;
}

int front(Queue *q) {
    if (isEmpty(q))
        return INT_MIN;
    return q->array[q->front];
}

int rear(Queue *q) {
    if (isEmpty(q))
        return INT_MIN;
    return q->array[q->rear];
}

void printQueue(Queue *q) {
    for (int i=q->front; i<=q->rear; ++i) {
        printf("%d ", q->array[i]);
    }
    printf("\n");
}

// int main(void) {
//     Queue *q = createQueue(5);
//     enqueue(q, 2);
//     enqueue(q, 2);
//     enqueue(q, 2);
//     enqueue(q, 2);
//     enqueue(q, 2);
//     dequeue(q);
//     printQueue(q);
// }