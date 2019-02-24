#include <iostream>

using namespace std;

int mergeLists(int* a, int s, int p, int e){
    int I = 0;
    
    if( (e-p==0) or (p-s==0) )
        return 0;
    
    int a0;
    if( a[s] > a[p] ){
        a0 = a[p];
        for(int j=p-1; j>s-1; j--){
            a[j+1] = a[j];
        }
        a[s] = a0;
        I += p - s;
        I += mergeLists(a, s+1, p+1, e);
    }
    else{
        I += mergeLists(a, s+1, p, e);
    }
    return I;
}

int sort(int* a, int start, int end){
    int I = 0;
    int l = end - start;
    
    int a0;
    if(l==2){
        if(a[start]>a[start+1]){
            a0 = a[start];
            a[start] = a[start+1];
            a[start+1] = a0;
            return 1;
        }
        else{
            return 0;
        }
    }
    if(l<=1)
        return 0;
    
    int point = (start+end+1)/2;
    I += sort(a, start, point);
    I += sort(a, point, end);
    I += mergeLists(a, start, point, end);
    return I;    
}

int main(){
    
    int n;
    cin >> n;

    int* arr = new int [n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    int inv = sort(arr, 0, n);
    cout << inv << endl;
    return 0;
}
