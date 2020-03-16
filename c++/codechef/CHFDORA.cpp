#include <iostream>

using namespace std;

int main()
{
        int t, n, m, **mat, i, j, s, pairs;
        cin >> t;
        while (t--)
        {
                cin >> n >> m;
                pairs = 0;
                mat = new int *[n];
                for (i = 0; i < n; ++i)
                {
                        mat[i] = new int[m];
                }
                for (i = 0; i < n; ++i)
                {
                        for (j = 0; j < m; ++j)
                        {
                                cin >> mat[i][j];
                        }
                }

                for (i = 0; i < n; ++i)
                {
                        for (j = 0; j < m; ++j)
                        {
                                s = 0;
                                while (1)
                                {
                                        if (i - s >= 0 && i + s < n && j - s >= 0 && j + s < m && mat[i][j - s] == mat[i][j + s] && mat[i - s][j] == mat[i + s][j])
                                        {
                                                ++pairs;
                                                ++s;
                                        }
                                        else
                                        {
                                                break;
                                        }
                                }
                        }
                }

                cout << pairs << endl;
                //delete
                for (i = 0; i < n; ++i)
                {
                        delete[] mat[i];
                }
                delete[] mat;
        }
}
