#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define ln '\n'

typedef vector<ll> vll;

int main()
{
    int n;
    cin >> n;
    vll numbers(n);
    for (int i = 0; i < n; i++)
    {
        cin >> numbers[i];
    }
    ll past = 0;
    ll best = -1e18;

    for(int i = 0; i < n; i++)
    {
        if(past >= 0)
        {
            past += numbers[i];
        }else {
            past = numbers[i];
        }
        best = max(best, past);
    }
    cout << best;

    return 0;
}