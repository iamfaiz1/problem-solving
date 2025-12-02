#include <bits/stdc++.h>
using namespace std;

using EdgeList = vector<pair<int, int>>;

vector<vector<int>> buildAdj(const EdgeList &edges, int n) {
    vector<vector<int>> adj(n + 1);
    for (auto [u, v] : edges) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    return adj;
}

vector<int> normalize_cycle(vector<int> c) {
    if (c.empty()) return c;
    int n = c.size();
    int pos = min_element(c.begin(), c.end()) - c.begin();
    rotate(c.begin(), c.begin() + pos, c.end());
    vector<int> rev(c.rbegin(), c.rend());
    pos = min_element(rev.begin(), rev.end()) - rev.begin();
    rotate(rev.begin(), rev.begin() + pos, rev.end());
    return min(c, rev);
}

void dfs_cycle(int u, int start, vector<int> &path, vector<bool> &vis,
               const vector<vector<int>> &adj, set<vector<int>> &cycles) {
    path.push_back(u);
    vis[u] = true;
    for (int nxt : adj[u]) {
        if (nxt == start && path.size() >= 3) {
            cycles.insert(normalize_cycle(path));
        } else if (!vis[nxt] && nxt > path.front()) {
            dfs_cycle(nxt, start, path, vis, adj, cycles);
        }
    }
    vis[u] = false;
    path.pop_back();
}

vector<vector<int>> findCycles(const vector<vector<int>> &adj, int n) {
    set<vector<int>> cycleSet;
    for (int i = 1; i <= n; ++i) {
        vector<int> path;
        vector<bool> vis(n + 1, false);
        dfs_cycle(i, i, path, vis, adj, cycleSet);
    }
    return {cycleSet.begin(), cycleSet.end()};
}

EdgeList applyPermutation(const EdgeList &edges, const vector<int> &perm) {
    EdgeList newEdges;
    for (auto [u, v] : edges) {
        int nu = perm[u], nv = perm[v];
        if (nu > nv) swap(nu, nv);
        newEdges.push_back({nu, nv});
    }
    sort(newEdges.begin(), newEdges.end());
    return newEdges;
}

EdgeList canonical(const EdgeList &edges) {
    EdgeList e = edges;
    sort(e.begin(), e.end());
    return e;
}

int compute_rotations() {
    int e;
    cin >> e;
    EdgeList g1, g2;
    int n = 0;

    for (int i = 0; i < e; ++i) {
        int u, v;
        cin >> u >> v;
        if (u > v) swap(u, v);
        g1.push_back({u, v});
        n = max({n, u, v});
    }
    sort(g1.begin(), g1.end());

    for (int i = 0; i < e; ++i) {
        int u, v;
        cin >> u >> v;
        if (u > v) swap(u, v);
        g2.push_back({u, v});
        n = max({n, u, v});
    }
    sort(g2.begin(), g2.end());

    if (g1 == g2) return 0;

    queue<pair<EdgeList, int>> q;
    map<EdgeList, int> dist;

    q.push({g1, 0});
    dist[g1] = 0;

    while (!q.empty()) {
        auto [curr, steps] = q.front();
        q.pop();

        if (curr == g2) return steps;

        auto adj = buildAdj(curr, n);
        auto cycles = findCycles(adj, n);

        for (auto &cyc : cycles) {
            for (int dir = 0; dir < 2; ++dir) {
                vector<int> perm(n + 1);
                iota(perm.begin(), perm.end(), 0);
                for (int i = 0; i < (int)cyc.size(); ++i) {
                    int from = cyc[i];
                    int to = cyc[(i + (dir == 0 ? 1 : -1) + cyc.size()) % cyc.size()];
                    perm[from] = to;
                }
                auto newGraph = applyPermutation(curr, perm);
                newGraph = canonical(newGraph);
                if (!dist.count(newGraph)) {
                    dist[newGraph] = steps + 1;
                    q.push({newGraph, steps + 1});
                }
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << compute_rotations();
    return 0;
}