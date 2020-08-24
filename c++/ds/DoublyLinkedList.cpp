#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* prev;
    Node* next;
    Node(int key): data(key), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList {
public:
    Node* head;
    Node* tail;

    DoublyLinkedList(): head(nullptr), tail(nullptr) {}

    void push_back(int key) {
        Node* new_node = new Node(key);
        if (tail == nullptr) {
            tail = new_node;
            head = new_node;
            return;
        }
        tail->next = new_node;
        new_node->prev = tail;
        tail = new_node;
    }

    void push_front(int key) {
        Node* new_node = new Node(key);
        if (head == nullptr) {
            tail = new_node;
            head = new_node;
            return;
        }
        new_node->next = head;
        head->prev = new_node;
        head = new_node;
    }

    bool pop_back() {
        if (tail == nullptr) {
            return false;
        }
        Node* prev_node = tail->prev;
        free(tail);
        tail = prev_node;
        tail->next = nullptr;
        if (tail == nullptr) {
            head = nullptr;
        }
        return true;
    }

    bool pop_front() {
        if (head == nullptr) {
            return false;
        }
        Node* next_node = head->next;
        free(head);
        head = next_node;
        head->prev = nullptr;
        if (head == nullptr) {
            tail = nullptr;
        }
        return true;
    }

    void delete_all_instances(int key) {
        if (head == nullptr) {
            return;
        }
        Node* temp_head = new Node(-1);
        temp_head->next = head;
        Node* temp = temp_head;
        while (temp->next != nullptr) {
            if (temp->next->data == key) {
                Node* next_next = temp->next->next;
                free(temp->next);
                temp->next = next_next;
                if (next_next != nullptr) {
                    next_next->prev = temp;
                }
            }
            else {
                temp = temp->next;
            }
        }
    }

    void print() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main() {
    DoublyLinkedList dll;
    dll.push_back(1);
    dll.push_back(5);
    dll.push_front(3);
    dll.push_front(8);
    dll.push_back(2);
    dll.push_back(6);
    dll.print();
    dll.pop_back();
    dll.print();
    dll.push_front(7);
    dll.print();
    dll.pop_front();
    dll.print();
}
