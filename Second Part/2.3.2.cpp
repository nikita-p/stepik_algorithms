//Параллельная обработка

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Comp{
public:
     bool operator ()(pair<long int,long int> &a, pair<long int,long int> &b){
        if( a.second < b.second )
            return false;
        if( a.second == b.second && a.first < b.first )
            return false;
        return true;
    }
};

int main(){

    long int num_proc, n;
    cin >> num_proc >> n;
    priority_queue< pair<long int, long int>, vector<pair<long int,long int>>, Comp > h;
    for(long int i=0; i<num_proc; i++)
        h.push({i, 0});
    
    pair<long int, long int> pp;
    long int t;
    
    for(long int i=0; i<n; i++){
        cin >> t;
        pp = h.top();
        h.pop();
        cout << pp.first << ' ' << pp.second << endl;
        pp.second += t;
        h.push(pp);
    }
    
    return 0;
}
