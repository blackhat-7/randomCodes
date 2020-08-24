#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <queue>
#include <stack>

using namespace std;

void vectors();
void sets();
void maps();
void algos();
void pq_q_stack();


int main()
{ 
    string s1, s2;
    cin >> s1 >> s2;
    cout << s1.compare(s2) << endl;
    size_t pos = s1.find('5');
    if (pos != string::npos)
        cout << "Found at : " << pos << endl;
    else
        cout << "Not found" << endl;
    
    string s3 = s1.substr(0, 3);
    cout << s3 << endl;
}


void vectors()
{
    cout << "Hello World" << endl;
    vector<int> v = {1,7,23,7,3,7,46,7,9};
    sort(v.begin(), v.end());
    for(auto i : v) {
        cout << i << " ";
    }
    cout << endl;
    bool present = binary_search(v.begin(), v.end(), 7);
    cout << present << endl;
    vector<int>::iterator itr1 = lower_bound(v.begin(), v.end(), 7);
    vector<int>::iterator itr2 = upper_bound(v.begin(), v.end(), 7);
    cout << *itr1 << " " << *itr2 << endl;
    cout << "Number of 7s : " << itr2 - itr1 << endl;
    vector<int> v1 = {1,2,3,4};
    v.insert(v1.begin()+2, 5);
    cout << v1[2] << endl;
}

void sets()
{
    set<int> s;
    for (int i=0; i<10; i++) {
        s.insert(rand()%100);
    }
    for (auto i : s) cout << i << " ";
    cout << endl;
    int x = 0;
    auto it1 = s.find(x);
    if (it1 != s.end()) {
        cout << *it1 << " is present" << endl;
    } else {
        cout << x << " not present" << endl;
    }
    auto it2 = s.upper_bound(x);
    auto it3 = s.lower_bound(x);
    cout << *it2 << " " << *it3 << endl;
}

void maps()
{
    map<int,int> m;
    for (int i=0; i<10; i++) {
        m[rand()%10] = rand()%10;
    }

    for (auto pair : m) {
        cout << pair.first << "=" << pair.second << " ";
        m[pair.first]++;
    }
    cout << endl;

    for (auto pair : m) {
        cout << pair.first << "=" << pair.second << " ";
    }
    cout << endl;
}

void algos()
{
    vector<int> v = {4,6,2,4,6,3};
    auto it = find(v.begin(), v.end(), 4);
    v.erase(v.begin() + distance(v.begin(), it));
    for (auto i : v) {
        cout << i << endl;
    }
    cout << v.size() << endl;
    int n = 3;
    int arr[n][n];
    fill(arr[0], arr[0] + n*n, 1);
    for (int i=0; i<sizeof(arr)/sizeof(arr[0]); i++) {
        for (int j=0; j<sizeof(arr[0])/sizeof(arr[0][0]); j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    cout << __gcd(16, 26) << endl;
}

void pq_q_stack()
{
    cout << "Priority Queues : \n";
    priority_queue<char, vector<char>, greater<char>> pq;
    pq.push('j');
    pq.push('d');
    pq.push('e');
    pq.push('u');
    pq.push('h');
    cout << pq.top() << endl;
    pq.pop();
    cout << pq.top() << endl;

    cout << "Stacks : \n";
    stack<int> st;
    st.push(2);
    st.push(4);
    st.push(7);
    st.push(221);
    cout << st.top() << endl;
    st.pop();
    cout << st.top() << endl;

    cout << "Queues : \n";
    queue<char> q;
    q.push('a');
    q.push('g');
    q.push('%');
    q.push('7');
    cout << q.front() << endl;
    q.pop();
    cout << q.front() << endl;

    cout << "Deques : \n";
    deque<int> dq;
    dq.push_back(4);
    dq.push_back(7);
    dq.push_front(2);
    dq.push_back(8);
    dq.push_front(9);
    cout << dq.front() << " " << dq.back() << endl;
    dq.pop_back();
    dq.pop_front();
    cout << dq.front() << " " << dq.back() << endl;
}