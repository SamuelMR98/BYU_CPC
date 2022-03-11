#include <iostream>
#include <vector>
#include <string>

using std :: cout;
using std :: cin;
using std :: endl;
using std :: vector;
using std :: string;

int main(){
    vector<string> echo;
    int size = 0;
    cin >> size;

    for (int i = 0; i < size; i++){
        string str = "";
        cin >> str;
        echo.push_back(str);
    }

    for (int i = 0; i < size; i++){
        if (i % 2 != 0){
            cout << echo[i] << endl;
        }
    }



    return 0;
}