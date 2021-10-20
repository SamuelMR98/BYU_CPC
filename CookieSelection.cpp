#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool asc (int i,int j) { return (i<j); }

int main(){
    vector<int> cookies;
    char c;
    
    if(c == '#'){
        sort(cookies.begin(), cookies.end(), asc);

        if((cookies.size()%2) == 0){
            int index = (cookies.size() / 2) + 1;
            cout << cookies[index];
            cookies.erase(cookies.begin() + index);
        }else{
            int index = (cookies.size() + 1) / 2;
            cout << cookies[index];
            cookies.erase(cookies.begin() + index);
        }
    }
    
   
}