#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    vector<int> students;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int id;
        cin >> id;
        students.push_back(id);
    }
    bool interate = true;
    while (interate){
        int changes = 0;
        for (int i = 0; i < n; i++){
            if (students[i] > students[i + 1]){
                if (i + 1 < n) {
                    swap(students[i], students[i + 1]);
                    changes++;
                }
            }
            else
            {
                continue;
            }
        }
        cout << changes << endl;
        if(changes == 0){
            interate = false;
        }
    }
}