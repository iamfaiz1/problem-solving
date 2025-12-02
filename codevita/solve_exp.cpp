#include <bits/stdc++.h>
using namespace std;

vector<string> splitBlocksWithStep(const vector<string> &lines, int step) {
    int maxw = 0;
    for (auto &r : lines) maxw = max(maxw, (int)r.size());
    vector<string> norm = lines;
    for (auto &r : norm) if ((int)r.size() < maxw) r += string(maxw - r.size(), ' ');
    int cols = maxw;
    if (cols < 3) return {};
    int count = (cols + (step - 3)) / step;
    vector<string> blocks;
    for (int i = 0; i < count; ++i) {
        int start = i * step;
        string pattern = "";
        for (int r = 0; r < 3; ++r) {
            string row = norm[r];
            if (start + 3 > (int)row.size()) row += string(start + 3 - row.size(), ' ');
            pattern += row.substr(start, 3);
        }
        blocks.push_back(pattern);
    }
    return blocks;
}

vector<string> splitBlocksAuto(const vector<string> &lines, int expectedCount = -1) {
    vector<string> b4 = splitBlocksWithStep(lines, 4);
    vector<string> b3 = splitBlocksWithStep(lines, 3);
    if (expectedCount > 0) {
        if ((int)b4.size() == expectedCount) return b4;
        if ((int)b3.size() == expectedCount) return b3;
    }
    auto nonempty = [](const vector<string> &v){
        int c = 0;
        for (auto &p : v) {
            bool allzero = true;
            for (char ch : p) if (ch != ' ') { allzero = false; break; }
            if (!allzero) ++c;
        }
        return c;
    };
    int n4 = nonempty(b4), n3 = nonempty(b3);
    return n4 >= n3 ? b4 : b3;
}

string blockToBits(const string &blk) {
    string bits;
    for (char c : blk) bits.push_back(c == ' ' ? '0' : '1');
    return bits;
}

map<string,string> parsePatternsAuto(const vector<string> &lines, const vector<string> &symbols) {
    vector<string> blocks = splitBlocksAuto(lines, (int)symbols.size());
    map<string,string> dict;
    for (size_t i = 0; i < symbols.size() && i < blocks.size(); ++i) {
        string key = blockToBits(blocks[i]);
        dict[key] = symbols[i];
    }
    return dict;
}

vector<string> parseExpressionAuto(const vector<string> &lines, const map<string,string> &allPatterns) {
    vector<string> blocks = splitBlocksAuto(lines, -1);
    vector<string> tokens;
    string numbuf = "";
    for (auto &blk : blocks) {
        string key = blockToBits(blk);
        auto it = allPatterns.find(key);
        if (it != allPatterns.end()) {
            string sym = it->second;
            if (sym.size() == 1 && isdigit(sym[0])) numbuf.push_back(sym[0]);
            else {
                if (!numbuf.empty()) { tokens.push_back(numbuf); numbuf.clear(); }
                tokens.push_back(sym);
            }
        }
    }
    if (!numbuf.empty()) tokens.push_back(numbuf);
    return tokens;
}

string bitOr(const string &a, const string &b) {
    int L = max((int)a.size(), (int)b.size());
    string A(L - (int)a.size(), '0'); A += a;
    string B(L - (int)b.size(), '0'); B += b;
    string r; r.reserve(L);
    for (int i = 0; i < L; ++i) r.push_back((A[i]=='1' || B[i]=='1') ? '1' : '0');
    return r;
}

string bitAnd(const string &a, const string &b) {
    int L = max((int)a.size(), (int)b.size());
    string A(L - (int)a.size(), '0'); A += a;
    string B(L - (int)b.size(), '0'); B += b;
    string r; r.reserve(L);
    for (int i = 0; i < L; ++i) r.push_back((A[i]=='1' && B[i]=='1') ? '1' : '0');
    return r;
}

string bitNot(const string &a) {
    string r; r.reserve(a.size());
    for (char c : a) r.push_back(c=='1' ? '0' : '1');
    return r;
}

string numberToBinary(const string &num, const map<string,string> &digitRev) {
    string out;
    for (char ch : num) {
        string key(1, ch);
        auto it = digitRev.find(key);
        if (it != digitRev.end()) out += it->second;
        else out += string(9, '0');
    }
    return out;
}

string binaryToNumber(const string &bin, const map<string,string> &binary2digit) {
    if (bin.empty()) return "0";
    int L = (int)bin.size();
    int rem = L % 9;
    string s = bin;
    if (rem != 0) s = string(9 - rem, '0') + s;
    string out;
    for (int i = 0; i < (int)s.size(); i += 9) {
        string chunk = s.substr(i, 9);
        auto it = binary2digit.find(chunk);
        if (it != binary2digit.end()) out += it->second;
        else out += '0';
    }
    int p = 0;
    while (p+1 < (int)out.size() && out[p] == '0') ++p;
    return out.substr(p);
}

string evaluateTokens(const vector<string> &tokens, const map<string,string> &digitRev) {
    stack<string> val;
    stack<string> op;
    auto apply = [&](const string &oper){
        if (oper == "~") {
            if (val.empty()) { val.push(string(9,'0')); return; }
            string a = val.top(); val.pop();
            val.push(bitNot(a));
        } else {
            if (val.empty()) { val.push(string(9,'0')); return; }
            string b = val.top(); val.pop();
            string a = val.empty() ? string(9,'0') : val.top(); if(!val.empty()) val.pop();
            if (oper == "|") val.push(bitOr(a,b));
            else if (oper == "&") val.push(bitAnd(a,b));
        }
    };
    auto prec = [&](const string &o)->int {
        if (o == "~") return 3;
        if (o == "|") return 2;
        if (o == "&") return 1;
        return 0;
    };
    for (auto &t : tokens) {
        if (t == "(") op.push(t);
        else if (t == ")") {
            while (!op.empty() && op.top() != "(") { string o = op.top(); op.pop(); apply(o); }
            if (!op.empty() && op.top() == "(") op.pop();
        } else if (t == "~" || t == "|" || t == "&") {
            while (!op.empty() && op.top() != "(" && prec(op.top()) >= prec(t)) { string o = op.top(); op.pop(); apply(o); }
            op.push(t);
        } else val.push(numberToBinary(t, digitRev));
    }
    while (!op.empty()) { string o = op.top(); op.pop(); apply(o); }
    return val.empty() ? string() : val.top();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<string> all(9);
    for (int i = 0; i < 9; ++i) getline(cin, all[i]);
    vector<string> digitLines = {all[0], all[1], all[2]};
    vector<string> opLines = {all[3], all[4], all[5]};
    vector<string> exprLines = {all[6], all[7], all[8]};
    vector<string> digits = {"0","1","2","3","4","5","6","7","8","9"};
    vector<string> ops = {"|","&","~","(",")"};
    auto digitPatterns = parsePatternsAuto(digitLines, digits);
    auto opPatterns = parsePatternsAuto(opLines, ops);
    map<string,string> digitRev, binary2digit;
    for (auto &p : digitPatterns) { binary2digit[p.first] = p.second; digitRev[p.second] = p.first; }
    map<string,string> allPatterns = digitPatterns;
    for (auto &p : opPatterns) allPatterns[p.first] = p.second;
    auto tokens = parseExpressionAuto(exprLines, allPatterns);
    string resBin = evaluateTokens(tokens, digitRev);
    string ans = binaryToNumber(resBin, binary2digit);
    cout << ans;
    return 0;
}