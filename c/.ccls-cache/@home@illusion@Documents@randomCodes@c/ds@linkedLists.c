#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    char data;
    struct Node *next;
} Node;

Node *append(Node **head, char data)
{
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;
    if (*head == NULL)
    {
        *head = new_node;
        return *head;
    }
    Node *temp = *head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = new_node;
    return new_node;
}

void _deleteList(Node *node)
{
    if (node != NULL)
    {
        _deleteList(node->next);
        free(node);
    }
}
void deleteList(Node **head)
{
    _deleteList(*head);
    *head = NULL;
}

void printList(Node **head)
{
    Node *temp = *head;
    while (temp != NULL)
    {
        printf("%c ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main(void)
{
    Node *head = NULL;
    append(&head, 'a');
    append(&head, 'b');
    append(&head, 'c');
    printList(&head);
    deleteList(&head);
}