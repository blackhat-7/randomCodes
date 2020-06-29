// { Driver Code Starts
#include<iostream>
#include<stdio.h>
using namespace std;

/* Link list Node */
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};

int intersectPoint(struct Node* head1, struct Node* head2);

void append(struct Node** head_ref, struct Node **tail_ref, int new_data)
{
    struct Node* new_node = new Node(new_data);
    if (*head_ref == NULL)
        *head_ref = new_node;
    else
        (*tail_ref)->next = new_node;
    *tail_ref = new_node;
}

/* Driver program to test above function*/
int main()
{
    int T,i,n1, n2, n3,l,k;

    cin>>T;
    while(T--)
    {
        cin>>n1>>n2>>n3;

        struct Node *head1 = NULL,  *tail1 = NULL;
        for(i=1; i<=n1; i++)
        {
            cin>>l;
            append(&head1, &tail1, l);
        }
        struct Node *head2 = NULL,  *tail2 = NULL;
        for(i=1; i<=n2; i++)
        {
            cin>>l;
            append(&head2, &tail2, l);
        }
        struct Node *head3 = NULL,  *tail3 = NULL;
        for(i=1; i<=n3; i++)
        {
            cin>>l;
            append(&head3, &tail3, l);
        }

        if (tail1 != NULL)
        tail1->next = head3;
        if (tail2 != NULL)
        tail2->next = head3;

        cout << intersectPoint(head1, head2) << endl;
    }
    return 0;
}

// } Driver Code Ends


/* Linked List Node
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}; */

/* Should return data of intersection point of two linked
   lists head1 and head2.
   If there is no intersecting point, then return -1. */
void recursive(Node *head1, Node *head2, int *data, int *found)
{
    if (head1->next != NULL && head2->next != NULL) {
        recursive(head1->next, head2->next, data, found);
    }
    else if (head1->next != NULL) {
        recursive(head1->next, head2, data, found);
    }
    else if (head2->next != NULL) {
        recursive(head1, head2->next, data, found);
    }
    if (!(*found) && head1 != head2) {
        if (head1->next == NULL) 
            *data = -1;
        else
            *data = head1->next->data;
        *found = 1;
    }
}

int intersectPoint(Node* head1, Node* head2)
{
    int n = (head1 == NULL) ? 0 : 1;
    int m = (head2 == NULL) ? 0 : 1;
    if (head1 == NULL || head2 == NULL) {
        return -1;
    }
    Node *head1_temp = head1;
    Node *head2_temp = head2;
    while(head1_temp->next != NULL) {
        ++n;
        head1_temp = head1_temp->next;
    }
    while(head2_temp->next != NULL) {
        ++m;
        head2_temp = head2_temp->next;
    }
    if (n > m) 
    {
        head1_temp = head1; head2_temp = head2;
    }
    else
    {
        head1_temp = head2; head2_temp = head1;
        int x = n; n = m; m = x;
    }
    while(n != m) {
        head1_temp = head1_temp->next; --n;
    }
    int ans = -1;
    int found = 0;
    recursive(head1_temp, head2_temp, &ans, &found);
    return ans;
}

