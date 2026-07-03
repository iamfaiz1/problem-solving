#include <stdio.h>
#include <iostream>
#include <unordered_map>
using namespace std;

class solution
{
public:
    int romanToInt(string s){
        // map declaration
        unordered_map<string, int> mp = {
            {"M", 1000},
            {"D", 500},
            {"C", 100},
            {"L", 50},
            {"X", 10},
            {"V", 5},
        };
        int ans;
        int prev = 0;
        int cur;

        for(auto c: s){
            cur = mp[c];
            if(cur >= prev)
                ans+= cur;
            else{
                ans -= cur;
            }
            cur = prev;
        }
        return ans;

    }
};