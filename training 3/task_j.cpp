#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main(){
    int n;
    cin >> n;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    for (int i = 0; i < n; i++){ 
        cin >> b[i];
    }

    long long sum_a = accumulate(a.begin(), a.end(), 0LL);
    long long sum_b = accumulate(b.begin(), b.end(), 0LL);

    if (sum_a > sum_b){
        cout << -1 << endl;
        return 0;
    }

    int left = 0, right = n;
    int min_k = -1;

    while (left <= right){
        int k = (left + right) / 2;
        bool flag = true;

        vector<long long> remaining_people = a;
        int p = 0;

        for (int i = 0; i < n; i++){
            while (p < n && remaining_people[p] == 0){
                p++;
            }
            if (p < n && p < i - k){
                flag = false;
                break;
            }
            long long cap = b[i];
            while (cap > 0){
                while (p < n && remaining_people[p] == 0){
                    p++;
                }
                if (p >= n) break;
                if (p > i + k) break;
                long long take = min(cap, remaining_people[p]);
                remaining_people[p] -= take;
                cap -= take;
                if (remaining_people[p] == 0){
                    p++;
                }
            }
        }

        if (flag){
            while (p < n && remaining_people[p] == 0){
                p++;
            }
            if (p < n){
                flag = false;
            }
        }

        if (flag){
            min_k = k;
            right = k - 1;
        } else{
            left = k + 1;
        }
    }
    cout << min_k;
    return 0;
}
