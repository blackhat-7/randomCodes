#include <iostream>
using namespace std;


int workbook(int n, int k, int book[])
{
    int page = 1;
    int special = 0;
    for (int i=0; i<n; ++i)
    {
        int temp = book[i];
        for (int start=1, end = (k<temp) ? k : temp; temp>0;start=end+1, end += (k<temp) ? k : temp)
        {
            if (page >= start && page <= end)
            {
                ++special;
            }
            ++page;
            temp-=k;
        }
    }
    return special;
}

int main()
{
    int n, k, *book;
    cin >> n >> k;
    book = new int[n];

    for (int i=0; i<n; ++i)
    {
        cin >> book[i];
    }
    int result = workbook(n, k, book);
    cout << result << endl;
}
