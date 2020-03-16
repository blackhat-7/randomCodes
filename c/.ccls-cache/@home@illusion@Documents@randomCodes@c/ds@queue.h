#ifndef __QUEUE_H
#define __QUEUE_H

typedef struct Queue Queue;

Queue *createQueue(int cap);
int isFull(Queue *q);
int isEmpty(Queue *q);
void enqueue(Queue *q, int data);
int dequeue(Queue *q);
int front(Queue *q);
int rear(Queue *q);
void printQueue(Queue *q);

#endif
