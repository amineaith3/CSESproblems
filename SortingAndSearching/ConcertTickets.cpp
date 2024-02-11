#include <bits/stdc++.h>

using namespace std;
#define ln '\n'
typedef long long ll;
int main() {
    int n, m;
    cin >> n >> m;
    vector<int> tickers(n);
    vector<int> customers(m);
    set<pair<int, int>> sortedTickets;
    for (int i = 0; i < n; i++) {
        cin >> tickers[i];
        sortedTickets.insert({tickers[i], i});
    }
    for(int i = 0; i < m; i++) {
        cin >> customers[i];
    }
    for(int i =0; i <m; i++)
    {
        auto match = sortedTickets.lower_bound({customers[i]+1, 0});
        if(match == sortedTickets.begin()){
            cout << -1 << ln;
        }
        else{
            match--;
            cout << match->first << ln;
            sortedTickets.erase(match);
        }
    }
    
    return 0;
}
