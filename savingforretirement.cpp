#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int by;
    int bry;
    int bs;
    int ay;
    int as;

    int obj;
    cin >> by >> bry >> bs >> ay >> as;

    obj = (bry - by) * bs;

    int ary = (obj / as) + ay + 1;

    cout << ary << endl;
}