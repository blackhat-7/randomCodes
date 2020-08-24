#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;


bool ispositive(int x) {
    return x >= 0;
}

int main() {
    // int x = 100;
    // cout << log10(x) << floor(x) << endl;

    // int arr[] = {1,4,2,3,6,5};
    // int n = sizeof(arr)/sizeof(arr[0]);
    
    // cout << all_of(arr, arr + n, [](int x) { return x>0; }) << endl;
    
    // sort(arr, arr+n, [](int x, int y) { return x > y; });
    
    // for (auto x : arr) { cout << x << " "; }
    // cout << "\n";

    // vector<int> v(9);
    // for (int i=0; i<v.size(); ++i) {
    //     v.at(i) = i;
    // }
    // for (int i=v.size()-1; i>=0; --i) {
    //     cout << v.at(i) << " ";
    // }
    // cout << endl;
    // v.erase(v.begin()+3);
    // v.back() = 4;
    // for (auto i=v.rbegin(); i!=v.rend(); ++i) {
    //     cout << *i << " ";
    // }
    // cout << endl;

    // string s, replaceby = "%20";
    // getline(cin, s);
    // int index = 0;
    // while((index = s.find(" ", index)) != string::npos) {
    //     s.replace(index, 1, replaceby);
    //     index += replaceby.length();
    // }
    // cout << s << endl;
    // int a, b;
    // cin >> a >> b;
    // int arr[a][b];
    // for (int i=0; i<a; ++i) {
    //     for (int j=0; j<b; ++j) {
    //         arr[i][j] = i+j;
    //     }
    // }
    // for (int i=0; i<a; ++i) {
    //     for (int j=0; j<b; ++j) {
    //         cout << arr[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    unordered_map<int, vector<string>> lens_map;
    vector<string> strs;
    strs.push_back("uijndf");
    strs.push_back("uijsddf");
    strs.push_back("uijn32f");
    strs.push_back("uijawf");

    for(auto s : strs) {
        if (lens_map.find(s.length()) == lens_map.end()) {
            lens_map[s.length()] = vector<string>();
        }
        lens_map[s.length()].push_back(s);
    }
    int i = 0;
    for (auto item : lens_map) {
        cout << lens_map.bucket_size(i) << " ";
        for (auto str : item.second) {
            cout << str << " ";
        }
        cout << endl;
        i++;
    }
    cout << lens_map.bucket_count() << endl;
}