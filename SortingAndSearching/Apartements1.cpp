#include <iostream>
#include <algorithm>
#include <vector>
 
using namespace std;
#define ll long long
 
int main()
{
    int n, m;
    ll k;
    int counter = 0;
    cin >> n >> m >> k;
 
    vector<ll> applicants(n);
    vector<ll> apartments(m);
 
    for (int i = 0; i < n; i++)
    {
        cin >> applicants[i];
    }
 
    for (int j = 0; j < m; j++)
    {
        cin >> apartments[j];
    }
 
    sort(applicants.begin(), applicants.end());
    sort(apartments.begin(), apartments.end());
 
    int i = 0, j = 0;
 
    while (i < n && j < m)
    {
        if (abs(applicants[i] - apartments[j]) <= k)
        {
            counter++;
            i++;
            j++;
        }
        else if (applicants[i] < apartments[j])
        {
            i++;
        }
        else
        {
            j++;
        }
    }
 
    cout << counter << endl;
 
    return 0;
}
