#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define ln '\n'

typedef set<pair<ll, int>> splli;



int main()
{
    int n;
    cin >> n;
    splli numbers;
    int counter = 1;
    for(int i = 0; i  <n; i ++)
    {
        ll x;
        cin >> x;
        numbers.insert({x, i});
    }
    auto it = numbers.begin();
    for(int i = 0; i < n - 1; i++)
    {
        if(it->second > (++it)->second)
        {
            counter++;
        }
    }
    cout << counter;
}