#include <iostream>
#include <string>

using  std :: cout;
using std :: cin;
using std :: endl;
using std :: string;

int main() {
    string num = "";
    cin >> num;

    string result = "";
    result.push_back(num[1]);
    result.push_back(num[0]);
    cout << result;

    return 0;
}
