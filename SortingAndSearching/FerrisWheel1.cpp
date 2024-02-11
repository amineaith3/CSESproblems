#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vll;
 
 
int main()
{
    int n;
    ll x;
    cin >> n >> x;
    vll data(n);
    for(int i = 0; i < n; ++i)
    {
        cin >> data[i];
    }
    
    sort(data.begin(), data.end());
    int start = 0;
    int end = n - 1;
    ll count = 0;
 
    while(start <= end)
    {
        if(data[start] + data[end] <= x)
        {
            start++;
            end--;
        }
        else
        {
            end--;
        }
        count++;
    }
    cout << count;
}
