#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int *pn = new int, *pm = new int, *pq = new int, *pTemp = new int, *px = new int, *py = new int;
    cin >> *pn >> *pq;
    vector <vector<int>> a(*pn);

    for(int *pi=0; *pi<*pn; pi++) {
        cin >> *pm;
        for(int *pj=0; *pj<*pm; pj++) {
            cin >> *pTemp;
            a[*pi].push_back(*pTemp);
        }
    }

    for(int *pi=0; *pi<*pq; pi++) {
        cin >> *px >> *py;
        cout << a[*px][*py];
    }

    delete pn, pm, pq, pTemp, px, py;
    return 0;
}

