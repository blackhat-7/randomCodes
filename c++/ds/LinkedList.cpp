#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node* next;
};

class LinkedList
{
public:
    Node* head;

    LinkedList() { head = NULL; }
    
    void push_back(int val)
    {
        Node* temp = head;
        Node* new_node = new Node();
        new_node->data = val;
        new_node->next = NULL;

        if (temp == NULL) {
            head = new_node;
            return;
        }

        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = new_node;
    }

    void push_front(int val)
    {
        Node* new_node = new Node();
        new_node->data = val;
        new_node->next = head;
        head = new_node;
    }

    void delete_node(int val)
    {
        Node* temp = head;
        if (temp->data == val) {
            Node *next = head->next;
            free(head);
            head = next;
            return;
        }
        while(temp->next != NULL && temp->next->data != val) {
            temp = temp->next;
        }
        if (temp->next != NULL) {
            Node* next = temp->next->next;
            free(temp->next);
            temp->next = next;
        }
    }

    void print()
    {
        Node* temp = head;
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main()
{
    LinkedList LL;
    LL.push_back(2);
    LL.push_back(5);
    LL.push_back(7);
    LL.push_back(9);
    LL.push_back(4);
    LL.print();
    LL.push_front(2);
    LL.print();
    LL.delete_node(7);
    LL.print();
}