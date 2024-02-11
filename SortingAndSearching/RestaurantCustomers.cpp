#include <bits/stdc++.h>

using namespace std;
#define ln '\n'
typedef long long ll;
typedef pair<ll, int> plli;
typedef set<plli> splli;

int main() {
    int n;
    cin >> n;

    splli customers;

    for (int i = 0; i < n; i++) {
        ll arrival, departure;
        cin >> arrival >> departure;
        customers.insert({arrival, +1});
        customers.insert({departure, -1});
    }

    int ans = 0;
    int max_customers = 0;

    for (auto c : customers) {
        ans += c.second;
        max_customers = max(max_customers, ans);
    }

    cout << max_customers << ln;

    return 0;
}
