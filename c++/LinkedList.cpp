#include <bits/stdc++.h>
class Node
{
    public:
        int data;
        Node *next;
        Node(int v)
        {
            data = v;
            next = nullptr;
        }
};

class LinkedList
{
    public:
        Node *head = nullptr;

        void append(int v)
        {
            if (head==nullptr)
            {
                head = new Node(v);
            }
            else
            {
                Node *temp = head;
                while(temp->next!=nullptr)
                {
                    temp = temp->next;
                }
                temp->next = new Node(v);
            }
        }

        int pop(int x)
        {
            Node *pre = head;
            Node *temp = pre->next;
            while(temp != nullptr && temp->data!=x)
            {
                pre = pre->next;
                temp = temp->next;
            }
            pre->next = temp->next;
            return x;
        }

        int pop()
        {
            Node *temp = head;
            int x;
            if (temp->next==nullptr)
            {
                x = head->data;
                head = nullptr;
            }
            else
            {
                while(temp->next->next!=nullptr)
                {
                    temp = temp->next;
                }
                x = temp->next->data;
                temp->next = nullptr;
            }
            return x;
        }

        void print()
        {
            Node *temp = head;
            while(temp!=nullptr)
            {
                printf("%d ", temp->data);
                temp = temp->next;
            }
            printf("\n");
        }
};

int main()
{
    LinkedList ll;
    ll.append(1);
    ll.append(2);
    ll.append(3);
    ll.append(4);
    ll.pop(2);
    ll.pop();
    ll.print();
    return 0;
}
