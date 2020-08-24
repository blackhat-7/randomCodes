#include <bits/stdc++.h>
using namespace std;


struct Node
{
    int data;
    Node* left;
    Node* right;
    Node(int d): data(d), left(nullptr), right(nullptr) {}
};

class MyBT
{
public:
    Node* root;

    MyBT(): root(nullptr) {}

    void levelOrder()
    {
        queue<Node*> q;
        q.emplace(root);
        q.emplace(nullptr);
        while (q.size() > 1)
        {
            Node* node = q.front();
            q.pop();
            if (node == nullptr)
            {
                cout << endl;
                q.emplace(nullptr);
                continue;
            }
            cout << node->data << " ";
            if (node->left != nullptr)
                q.emplace(node->left);
            if (node->right != nullptr)
                q.emplace(node->right);
        }
        cout << endl;
    }

    bool is_complete() {
        bool flag = false;
        queue<Node*> q;
        q.emplace(root);
        while (!q.empty())
        {
            Node* n = q.front();
            q.pop();
            if (n->left != nullptr) {
                if (flag)
                    return false;
                q.emplace(n->left);
            } else {
                flag = true;
            }
            if (n->right != nullptr) {
                if (flag)
                    return false;
                q.emplace(n->right);
            } else {
                flag = true;
            }
        }
        return true;
    }

    void is_minHeap() {
        bool is_heap = true;
        bool is_complete = false;
        queue<Node*> q;
        q.emplace(root);
        while (!q.empty())
        {
            Node* n = q.front();
            q.pop();
            if (n->left != nullptr) {
                if (is_complete || n->left->data < n->data) {
                    is_heap = false;
                    break;
                }
                q.emplace(n->left);
            } else {
                is_complete = true;
            }
            if (n->right != nullptr) {
                if (is_complete || n->right->data < n->data) {
                    is_heap = false;
                    break;
                }
                q.emplace(n->right);
            } else {
                is_complete = true;
            }
        }
        if (is_heap)
            cout << "It's a min heap" << endl;
        else
            cout << "Not a min heap" << endl;
    }

    bool is_bst_util(Node* root, int min, int max) {
        if (root == nullptr)
            return true;
        if (root->data < min || root->data > max) {
            return false;
        }
        return is_bst_util(root->left, min, root->data) && is_bst_util(root->right, root->data, max);
    }
    
    void is_bst() {
        if (is_bst_util(root, INT_MIN, INT_MAX)) {
            cout << "Is a BST" << endl;
        } else {
            cout << "Not a BST" << endl;
        }
    }
    
    void all_nodes_at_dist_k_from_leaves_util(Node* root, unordered_set<Node*>& nodes, vector<Node*> path, int k) {
        if (root == nullptr)
            return;

        path.emplace_back(root);
        if (root->left == nullptr && root->right == nullptr) {
            if(path.size() > k)
                nodes.emplace(path[path.size()-k-1]);
            return;
        }
        all_nodes_at_dist_k_from_leaves_util(root->left, nodes, path, k);
        all_nodes_at_dist_k_from_leaves_util(root->right, nodes, path, k);
    }
    
    void all_nodes_at_dist_k_from_leaves(int k) {
        unordered_set<Node*> nodes;
        vector<Node*> path;
        all_nodes_at_dist_k_from_leaves_util(root, nodes, path, k);
        cout << "Nodes : ";
        for (Node* node : nodes) {
            cout << node->data << " ";
        }
        cout << endl;
    }

    void inorder_morris_traversal() {
        Node* curr = root;
        while (curr != nullptr) {
            if (curr->left == nullptr) {
                cout << curr->data << " ";
                curr = curr->right;
            }
            else {
                Node* pre = curr->left;
                while (pre->right != nullptr && pre->right != curr) {
                    pre = pre->right;
                }
                if (pre->right == nullptr) {
                    pre->right = curr;
                    curr = curr->left;
                } else {
                    cout << pre->right->data << " ";
                    pre->right = nullptr;
                    curr = curr->right;
                }
            }
        }
        cout << endl;
    }

    static void inorder_recursive(Node* root) {
        if (root != nullptr) {
            inorder_recursive(root->left);
            cout << root->data << " ";
            inorder_recursive(root->right);
        }
    }
    static void postorder_recursive(Node* root) {
        if (root != nullptr) {
            postorder_recursive(root->left);
            postorder_recursive(root->right);
            cout << root->data << " ";
        }
    }

    static void constructBT_inorder_postorder(int inorder[], int postorder[], int n) {
        unordered_map<int,int> indices;
        for (int i=0; i<n; i++)
            indices[inorder[i]] = i;

        int pindex =n-1;
        Node* new_root = constructBT_inorder_postorder_util(postorder, 0, n-1, indices, pindex);
        inorder_recursive(new_root);
        cout << endl;
        postorder_recursive(new_root);
        cout << endl;

    }
    
    static Node* constructBT_inorder_postorder_util(int postorder[], int low, int high, unordered_map<int,int> indices, int& pindex) {
        if (low > high)
            return nullptr;
        Node* curr = new Node(postorder[pindex--]);
        int index = indices[curr->data];
        curr->right = constructBT_inorder_postorder_util(postorder, index+1, high, indices, pindex);
        curr->left = constructBT_inorder_postorder_util(postorder, low, index-1, indices, pindex);
        return curr;
    } 

    void inorder_successors(){
        unordered_map<Node*,Node*> successors;
        Node* prev = nullptr;
        inorder_successors_util(root, successors, prev);
        for (auto s : successors) {
            string next = (s.second != nullptr) ? to_string(s.second->data) : "NULL";
            cout << s.first->data << " : " << next << endl;
        }
    }
    
    void inorder_successors_util(Node* node, unordered_map<Node*,Node*>& successors, Node*& prev) {
        if (node == nullptr)
            return;
        inorder_successors_util(node->left, successors, prev);
        if (prev != nullptr)
            successors[prev] = node;
        prev = node;
        inorder_successors_util(node->right, successors, prev);
    }
};



int main()
{
    MyBT bt;
    bt.root = new Node(15);
    bt.root->left = new Node(10);
    bt.root->right = new Node(20);
    bt.root->left->left = new Node(8);
    bt.root->left->right = new Node(12);
    bt.root->right->left = new Node(16);
    bt.root->right->right = new Node(25);
    bt.root->right->left->left = new Node(18);
    bt.levelOrder();
    bt.inorder_successors();
}

