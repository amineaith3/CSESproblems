#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define ln '\n'

typedef vector<ll> vll;



int main()
{
    int n;
    cin >> n;
    vll sticks(n);
    for(int i = 0; i < n; i++)
    {
        cin >> sticks[i];
    }

    sort(sticks.begin(), sticks.end());
    ll median = sticks[n/2];
    ll result = 0;
    for(int i = 0; i < n; i++)
    {
        result += abs(sticks[i] - median);
    }
    cout << result;
    
    return 0;
}
