#include <bits/stdc++.h>
using namespace std;

string keyFromVec(const vector<int>& v) {
    string s;
    s.reserve(v.size());
    for (int x : v) s.push_back(char('A' + x));
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    string w;
    cin >> w;
    cin.ignore();

    vector<string> shuffled(N), original(N);
    for (int i = 0; i < N; ++i) getline(cin, shuffled[i]);
    cin >> w;
    cin.ignore();
    for (int i = 0; i < N; ++i) getline(cin, original[i]);

    unordered_map<string, int> pos;
    for (int i = 0; i < N; ++i) pos[original[i]] = i;

    vector<int> start(N), target(N);
    for (int i = 0; i < N; ++i) start[i] = pos[shuffled[i]];
    iota(target.begin(), target.end(), 0);

    if (start == target) {
        cout << 0;
        return 0;
    }

    string ks = keyFromVec(start), kt = keyFromVec(target);
    unordered_map<string, int> dist1, dist2;
    queue<string> q1, q2;
    dist1[ks] = 0;
    dist2[kt] = 0;
    q1.push(ks);
    q2.push(kt);

    while (!q1.empty() && !q2.empty()) {
        if (q1.size() <= q2.size()) {
            int sz = q1.size();
            while (sz--) {
                string curk = q1.front();
                q1.pop();
                int d = dist1[curk];
                vector<int> cur(N);
                for (int i = 0; i < N; ++i) cur[i] = curk[i] - 'A';

                for (int i = 0; i < N; ++i) {
                    for (int j = i; j < N; ++j) {
                        vector<int> block(cur.begin() + i, cur.begin() + j + 1);
                        vector<int> rem;
                        rem.reserve(N - (j - i + 1));
                        for (int t = 0; t < N; ++t)
                            if (t < i || t > j) rem.push_back(cur[t]);
                        for (int p = 0; p <= (int)rem.size(); ++p) {
                            if (p == i) continue;
                            vector<int> nxt = rem;
                            nxt.insert(nxt.begin() + p, block.begin(), block.end());
                            string nk = keyFromVec(nxt);
                            if (dist1.find(nk) == dist1.end()) {
                                dist1[nk] = d + 1;
                                if (dist2.find(nk) != dist2.end()) {
                                    cout << dist1[nk] + dist2[nk];
                                    return 0;
                                }
                                q1.push(nk);
                            }
                        }
                    }
                }
            }
        } else {
            int sz = q2.size();
            while (sz--) {
                string curk = q2.front();
                q2.pop();
                int d = dist2[curk];
                vector<int> cur(N);
                for (int i = 0; i < N; ++i) cur[i] = curk[i] - 'A';

                for (int i = 0; i < N; ++i) {
                    for (int j = i; j < N; ++j) {
                        vector<int> block(cur.begin() + i, cur.begin() + j + 1);
                        vector<int> rem;
                        rem.reserve(N - (j - i + 1));
                        for (int t = 0; t < N; ++t)
                            if (t < i || t > j) rem.push_back(cur[t]);
                        for (int p = 0; p <= (int)rem.size(); ++p) {
                            if (p == i) continue;
                            vector<int> nxt = rem;
                            nxt.insert(nxt.begin() + p, block.begin(), block.end());
                            string nk = keyFromVec(nxt);
                            if (dist2.find(nk) == dist2.end()) {
                                dist2[nk] = d + 1;
                                if (dist1.find(nk) != dist1.end()) {
                                    cout << dist2[nk] + dist1[nk];
                                    return 0;
                                }
                                q2.push(nk);
                            }
                        }
                    }
                }
            }
        }
    }

    cout << -1;
    return 0;
}