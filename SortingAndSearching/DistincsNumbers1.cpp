#include <bits/stdc++.h>

using namespace std;
#define ll long long

int main()
{
    int n;
    cin >> n;
    set<int> x;
    for (int i=0; i < n; i++)
    {
        int s;
        cin >> s;
        x.insert(s);
    }
    cout << x.size();
}
