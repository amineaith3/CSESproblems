#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define ln '\n'

typedef vector<ll> vll;



int main()
{
    int n;
    cin >> n;
    vll coins(n);
    for(int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }
    sort(coins.begin(), coins.end());
    ll smallestSum = 1;

//smallest = 19
// 1 2 2 5 7 
// 
    for(int i = 0; i < n && smallestSum >= coins[i]; ++i)
    {
        smallestSum += coins[i];
    }
    cout << smallestSum;

    return 0;
}