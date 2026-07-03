#include<stdio.h>
#include<iostream>
using namespace std;

#include <unordered_map>

class solution{
    public:
        string intToRoman(int n){
            
            unordered_map<string, int> mp = {
            {"M", 1000},
            {"CM", 900},
            {"D", 500},
            {"CD", 400},
            {"C", 100},
            {"XC", 90},
            {"L", 50},
            {"XL", 40},
            {"X", 10},
            {"IX", 9},
            {"V", 5},
            {"IV", 4}
            };
        }
};

