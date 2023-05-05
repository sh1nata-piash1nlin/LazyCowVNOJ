#include <bits/stdc++.h>
using namespace std;
const int inf = 1000000007;
int dp[1005][1005][3];   //smalest area when we have i cows, using j <= K, and state. 
int N, K, B;
int testcase;

struct COW {
    int x, y;
    bool operator < (const COW &oxy) const {
    if (y < oxy.y || (y == oxy.y && x < oxy.x)) {
        return true;
    }
    return false;
    }
};


vector <COW> coww;

void updateMin(int &a, int b) {
    a = min(a, b);
}

int main () {
    cin >> testcase; 
    for (int testCase = 1; testCase <= testcase; testCase++) {
    cin >> N >> K >> B;
    coww.clear();
//state = 0: cow ith is covered by a 1-width square 
//state = 1: cow ith is covered by a 2-width square
//state = 2: cow ith is covered by a 1-width square and the other line: 1-width -> same col (pos of cow ith)

    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= K; j++) {
            for (int state = 0; state < 3; state++) {  
                dp[i][j][state] = inf;
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        int x, y;
        cin >> x >> y;
        coww.push_back((COW){x, y});
    }
    sort(coww.begin(), coww.end());

    dp[1][1][0] = 1;
    dp[1][1][1] = 2;

    if (K >= 2) {
        dp[1][2][2] = 2;
    }
    for (int i = 1; i < N; ++i) {
        for (int j = 1; j <= K; ++j) {
            for (int state = 0; state <= 2; ++state) {
                if (dp[i][j][state] == inf) {
                    continue;
                }
                int value = dp[i][j][state];
                if (j + 1 <= K) {
                    //cow i+1 o 1 chuong rieng biet, st= 0
                    updateMin(dp[i + 1][j + 1][0], value + 1);
                    //cow i+1 o 1 chuong rieng biet, st = 1     
                    updateMin(dp[i + 1][j + 1][1], value + 2);
                    //cow i+1 o st = 2 
                    if (j + 2 <= K) {
                        updateMin(dp[i + 1][j + 2][2], value + 2);
                    }
                }
                //chia truong hop 
                if (state == 0) {
                    if (j + 1 <= K) {  //state = 2 for i + 1 
                        updateMin(dp[i + 1][j + 1][2], value + coww[i].y - coww[i - 1].y + 1); 
                    }
                    if (coww[i].x == coww[i - 1].x){  //same line, keo chuong ra, no more chuong added 
                        updateMin(dp[i + 1][j][0], value + coww[i].y - coww[i - 1].y); 
                    }
                }
                else if (state == 1) {    //only 1 case 
                    updateMin(dp[i + 1][j][1], value + 2 * (coww[i].y - coww[i - 1].y)); 
                }  
                else {
                    if (coww[i].x != coww[i - 1].x) {    //khac hang keo dai chuong 
                        updateMin(dp[i + 1][j][0], value + coww[i].y - coww[i - 1].y); 
                    }
                    if (j + 1 <= K) {        //them chuong st = 2, 
                        updateMin(dp[i + 1][j + 1][2], value + coww[i].y - coww[i - 1].y + 1); 
                    }
                    updateMin(dp[i + 1][j][2], value + 2 * (coww[i].y - coww[i - 1].y)); 
                }
            }
        }
    }

    int ans = inf;
    for (int state = 0; state <= 2; ++state){
        updateMin(ans, dp[N][K][state]); 
    }
    cout << ans << endl;
}

return 0;
}                                                                                  