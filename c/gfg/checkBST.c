#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int key;
    struct Node *left;
    struct Node *right;
} Node;

Node *add(Node **root, int value)
{
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->key = value;
    if (*root == NULL)
    {
        *root = new_node;
        return new_node;
    }
    Node *pCrawl = *root;
    Node *prev = *root;
    while (pCrawl != NULL)
    {
        prev = pCrawl;
        if (value <= pCrawl->key)
        {
            pCrawl = pCrawl->left;
        }
        else if (value > pCrawl->key)
        {
            pCrawl = pCrawl->right;
        }
    }
    if (value <= prev->key)
        prev->left = new_node;
    else
        prev->right = new_node;
    return new_node;
}

void print_inorder(Node **root)
{
    if (*root != NULL)
    {
        print_inorder(&(*root)->left);
        printf("%d\n", (*root)->key);
        print_inorder(&(*root)->right);
    }
}

int main(void)
{
    int t;
    scanf("%d", &t);
    
}