#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int key;
    struct Node *left;
    struct Node *right;
} Node;

Node *addNode(Node **root, int value)
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

Node *deleteNode(Node **root, int val) {
    if (*root == NULL)
        return NULL;
    else if (val < (*root)->key) {
        (*root)->left = deleteNode(&(*root)->left, val);
    }
    else if (val > (*root)->key) {
        (*root)->right = deleteNode(&(*root)->right, val);
    }
    else {
        if ((*root)->left == NULL && (*root)->right == NULL) {
            free(*root);
            return NULL;
        }
        else if ((*root)->left == NULL) {
            Node *right = (*root)->right;
            free(*root);
            return right;
        }
        else if ((*root)->right == NULL) {
            Node *left = (*root)->left;
            free(*root);
            return left;
        }
        else {
            Node *left = (*root)->left;
            while(left->right != NULL) {
                left = left->right;
            }
            (*root)->key = left->key;
            (*root)->left = deleteNode(&(*root)->left, left->key);
            return *root;
        }
    }
    return *root;
}

void printInorder(Node **root)
{
    if (*root != NULL)
    {
        printInorder(&(*root)->left);
        printf("%d ", (*root)->key);
        printInorder(&(*root)->right);
    }
}

int getNodeCountInRange(Node **root, int l, int h) {
    if (*root == NULL)
        return 0;
    else if ((*root)->key >= l && (*root)->key <= h)
        return 1 + getNodeCountInRange(&(*root)->left, l, h) + getNodeCountInRange(&(*root)->right, l, h);
    else {
        if ((*root)->key < l) 
            return getNodeCountInRange(&(*root)->right, l, h);
        if ((*root)->key > h)
            return getNodeCountInRange(&(*root)->left, l, h);
    }
}

int main(void)
{
    Node *root = NULL;
    addNode(&root, 5);
    addNode(&root, 8);
    addNode(&root, 6);
    addNode(&root, 9);
    addNode(&root, 2);
    addNode(&root, 4);

    printf("%d\n", getNodeCountInRange(&root, 3, 8));
}