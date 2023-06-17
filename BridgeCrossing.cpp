#include <vector>
#include <math.h> 
int state[6]; 
int ans = 100005;

void backTrack(const int &n, bool flashLight, int totalTime, const std::vector <int> &times) {
    if (flashLight == false) {
        bool check = true; 
        for (int i = 0; i < n; i++) {
            if (state[i] == 0) {
                check = false; 
                break; 
            }
        }
        if (check == true) {
            ans = std::min(ans, totalTime); 
        }
        else {
            for (int i = 0; i < n; i++) {
                if (state[i] == 1) {
                    state[i] = 0; 
                    backTrack(n, !flashLight, totalTime + times[i], times); 
                    state[i] = 1; 
                }
            }
        }
    }
    else {
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (state[i] == 0 && state[j] == 0) {
                    state[i] = 1;
                    state[j] = 1; 
                    backTrack(n, !flashLight, totalTime + std::max(times[i], times[j]), times); 
                    state[i] = 0; 
                    state[j] = 0; 
                } 
            }
        }
    }
}

class BridgeCrossing {
    public: 
    int minTime(std::vector <int> times) {
    int n = (int) times.size(); 
    if (n == 1) {
        return times[0]; 
    }
    backTrack(n, true, 0, times);
    return ans;   
    }
};