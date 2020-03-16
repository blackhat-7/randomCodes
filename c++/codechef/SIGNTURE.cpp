#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t, n, m, count;
	string s;
	cin >> t;
	while (t--) {
		count = 0;
		cin >> n >> m;
		vector <vector<int>> a(m, vector<int>(n, 0));
		vector <vector<int>> b(m, vector<int>(n, 0));

		for (int i = 0; i < n; i++) {
			cin >> s;
			a[i][0] = s[0]; a[i][1] = s[1]; a[i][2] = s[2];
		}
		for (int i = 0; i < n; i++) {
			cin >> s;
			b[i][0] = s[0]; b[i][1] = s[1]; b[i][2] = s[2];
			for (int j = 0; j < m; j++) {
				count += a[i][j] ^ b[i][j];
			}
		}
		cout << count << endl;
	}
}