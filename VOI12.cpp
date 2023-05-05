#include <bits/stdc++.h>
using namespace std; 

struct NHAP
{
    int Ci, Ti; 
};

NHAP a[20004]; 
int n; 

bool check( vector <pair < int, int > > &a )
{
    sort(a.begin(), a.end());
    priority_queue <int, vector <int>, greater <int> > pq; 
    int i = 0; 
    for ( int columnn = 1; columnn <= n; ++columnn)
    {
        while (!pq.empty())
        {
            if (pq.top() < columnn)  // trường hợp khác hay, [1.2]
            {
                pq.pop();            //trường hợp nhỏ hơn thì vẫn vứt
            }                        //có nên = không? KHÔNG  
            else 
                break; 
        }
        while (i < n && a[i].first <= columnn)
        {
            pq.push(a[i].second);    //đẩy thẳng rx vô min HEAP 
            ++i; 
        }
        if (pq.empty() == true)
            return false; 
        else 
            pq.pop();      //cứ xóa. 
    }
    return true; 
}

int main()
{
    cin >> n; 
    for ( int i = 1; i <= n; ++i)
    {
        cin >> a[i].Ci >> a[i].Ti; 
    }

    int lo = 0; 
    int hi = 100000007; 
    int ans = -1; 
    while ( lo <= hi )
    {
        int time_middle = (lo + hi)/2; 
        vector <pair < int, int > > vt; 
        for ( int i = 1; i <= n; ++i)
        {       //tạo khoản hoạt động đi plz 
            vt.push_back(make_pair(max(1, a[i].Ci - time_middle/a[i].Ti), min(n, a[i].Ci + time_middle/a[i].Ti)));
        }
        if ( check(vt) == true )
        {
            ans = time_middle; 
            hi = time_middle - 1; 
        }
        else 
        {
            lo = time_middle + 1; 
        }
    }
    cout << ans; 
    return 0;
}