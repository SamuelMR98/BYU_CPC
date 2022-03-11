#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'sherlockAndAnagrams' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int sherlockAndAnagrams(string s) {
    int anagram = 0;
    vector<string> v(0);

    for(int i = 0, iRange = 1; (int)i < s.length() - 1; i++, iRange++) {
        v.clear();
        for(int j = 0; (int)j < s.length() - iRange + 1; j++) {
           v.push_back(s.substr(j, iRange));
        }

        for(int j = 0; (int)j < v.size(); j++) {
            sort(v[j].begin(), v[j].end());
        }

        for(int j = 0; (int)j < v.size(); j++) {
            for(int k = j + 1; (int)k < v.size(); k++) {
                if(v[j] == v[k]) {
                    anagram++;
                }
            }
        }
    }
    
    return anagram;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        int result = sherlockAndAnagrams(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}