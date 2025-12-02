#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

using namespace std;

int N;

typedef vector<vector<char>> Face;
typedef vector<Face> Cube;

Face rotateFace(const Face& face, bool clockwise) {
    Face newFace(N, vector<char>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (clockwise) {
                newFace[i][j] = face[N - 1 - j][i];
            } else {
                newFace[i][j] = face[j][N - 1 - i];
            }
        }
    }
    return newFace;
}

void turnLeft(Cube& cube) {
    Face temp = cube[4];
    cube[4] = cube[6];
    cube[6] = cube[2];
    cube[2] = cube[5];
    cube[5] = temp;
    cube[3] = rotateFace(cube[3], true);
    cube[1] = rotateFace(cube[1], false);
}

void turnRight(Cube& cube) {
    Face temp = cube[4];
    cube[4] = cube[5];
    cube[5] = cube[2];
    cube[2] = cube[6];
    cube[6] = temp;
    cube[3] = rotateFace(cube[3], false);
    cube[1] = rotateFace(cube[1], true);
}

void rotateFront(Cube& cube) {
    Face temp = cube[4];
    cube[4] = cube[3];
    cube[3] = cube[2];
    cube[2] = cube[1];
    cube[1] = temp;
    cube[5] = rotateFace(cube[5], true);
    cube[6] = rotateFace(cube[6], false);
}

void rotateBack(Cube& cube) {
    Face temp = cube[4];
    cube[4] = cube[1];
    cube[1] = cube[2];
    cube[2] = cube[3];
    cube[3] = temp;
    cube[5] = rotateFace(cube[5], false);
    cube[6] = rotateFace(cube[6], true);
}

void rotateLeft(Cube& cube) {
    Face temp = cube[3];
    cube[3] = cube[6];
    cube[6] = cube[1];
    cube[1] = cube[5];
    cube[5] = temp;
    cube[4] = rotateFace(cube[4], false);
    cube[2] = rotateFace(cube[2], true);
}

void rotateRight(Cube& cube) {
    Face temp = cube[3];
    cube[3] = cube[5];
    cube[5] = cube[1];
    cube[1] = cube[6];
    cube[6] = temp;
    cube[4] = rotateFace(cube[4], true);
    cube[2] = rotateFace(cube[2], false);
}

void topRowLeft(Cube& cube, int i) {
    vector<char> tempRow(N);
    for (int k = 0; k < N; ++k) tempRow[k] = cube[4][i][k];
    for (int k = 0; k < N; ++k) cube[4][i][k] = cube[6][i][k];
    for (int k = 0; k < N; ++k) cube[6][i][k] = cube[2][i][k];
    for (int k = 0; k < N; ++k) cube[2][i][k] = cube[5][i][k];
    for (int k = 0; k < N; ++k) cube[5][i][k] = tempRow[k];

    if (i == 0) cube[3] = rotateFace(cube[3], false);
    if (i == N - 1) cube[1] = rotateFace(cube[1], true);
}

void topRowRight(Cube& cube, int i) {
    vector<char> tempRow(N);
    for (int k = 0; k < N; ++k) tempRow[k] = cube[4][i][k];
    for (int k = 0; k < N; ++k) cube[4][i][k] = cube[5][i][k];
    for (int k = 0; k < N; ++k) cube[5][i][k] = cube[2][i][k];
    for (int k = 0; k < N; ++k) cube[2][i][k] = cube[6][i][k];
    for (int k = 0; k < N; ++k) cube[6][i][k] = tempRow[k];

    if (i == 0) cube[3] = rotateFace(cube[3], true);
    if (i == N - 1) cube[1] = rotateFace(cube[1], false);
}

void topColUp(Cube& cube, int j) {
    vector<char> tempCol(N);
    for (int k = 0; k < N; ++k) tempCol[k] = cube[1][k][j];
    for (int k = 0; k < N; ++k) cube[1][k][j] = cube[4][k][j];
    for (int k = 0; k < N; ++k) cube[4][k][j] = cube[3][k][j];
    for (int k = 0; k < N; ++k) cube[3][k][j] = cube[2][N - 1 - k][N - 1 - j];
    for (int k = 0; k < N; ++k) cube[2][N - 1 - k][N - 1 - j] = tempCol[k];

    if (j == 0) cube[5] = rotateFace(cube[5], true);
    if (j == N - 1) cube[6] = rotateFace(cube[6], false);
}

void topColDown(Cube& cube, int j) {
    vector<char> tempCol(N);
    for (int k = 0; k < N; ++k) tempCol[k] = cube[1][k][j];
    for (int k = 0; k < N; ++k) cube[1][k][j] = cube[2][N - 1 - k][N - 1 - j];
    for (int k = 0; k < N; ++k) cube[2][N - 1 - k][N - 1 - j] = cube[3][k][j];
    for (int k = 0; k < N; ++k) cube[3][k][j] = cube[4][k][j];
    for (int k = 0; k < N; ++k) cube[4][k][j] = tempCol[k];

    if (j == 0) cube[5] = rotateFace(cube[5], false);
    if (j == N - 1) cube[6] = rotateFace(cube[6], true);
}

void applyMove(Cube& cube, const string& instruction) {
    stringstream ss(instruction);
    string part1, part2, part3;
    ss >> part1 >> part2 >> part3;

    if (part2.empty()) {
    } else if (part3.empty()) {
        if (part1 == "turn" && part2 == "left") turnLeft(cube);
        else if (part1 == "turn" && part2 == "right") turnRight(cube);
        else if (part1 == "rotate" && part2 == "front") rotateFront(cube);
        else if (part1 == "rotate" && part2 == "back") rotateBack(cube);
        else if (part1 == "rotate" && part2 == "left") rotateLeft(cube);
        else if (part1 == "rotate" && part2 == "right") rotateRight(cube);
    } else {
        int idx = stoi(part2) - 1;
        string dir = part3;

        if (part1 == "base") { rotateFront(cube); rotateFront(cube); }
        else if (part1 == "back") { rotateBack(cube); }
        else if (part1 == "front") { rotateFront(cube); }
        else if (part1 == "left") { turnRight(cube); rotateFront(cube); }
        else if (part1 == "right") { turnLeft(cube); rotateFront(cube); }

        if (dir == "left") topRowLeft(cube, idx);
        else if (dir == "right") topRowRight(cube, idx);
        else if (dir == "up") topColUp(cube, idx);
        else if (dir == "down") topColDown(cube, idx);

        if (part1 == "base") { rotateBack(cube); rotateBack(cube); }
        else if (part1 == "back") { rotateFront(cube); }
        else if (part1 == "front") { rotateBack(cube); }
        else if (part1 == "left") { rotateBack(cube); turnLeft(cube); }
        else if (part1 == "right") { rotateBack(cube); turnRight(cube); }
    }
}

pair<bool, bool> checkCubeState(const Cube& cube) {
    bool isSolved = false;
    bool isOneOff = false;

    for (int f = 1; f <= 6; ++f) {
        map<char, int> counts;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                counts[cube[f][i][j]]++;
            }
        }

        int maxCount = 0;
        for (auto const& [key, val] : counts) {
            if (val > maxCount) {
                maxCount = val;
            }
        }

        if (maxCount == N * N) {
            isSolved = true;
            break;
        }
        if (maxCount == N * N - 1) {
            isOneOff = true;
        }
    }
    return {isSolved, isOneOff};
}

int main() {
    int K;
    cin >> N >> K;
    cin.ignore();

    Cube originalCube(7, Face(N, vector<char>(N)));
    for (int f = 1; f <= 6; ++f) {
        for (int i = 0; i < N; ++i) {
            string line;
            getline(cin, line);
            stringstream ss(line);
            for (int j = 0; j < N; ++j) {
                ss >> originalCube[f][i][j];
            }
        }
    }

    vector<string> instructions(K);
    for (int i = 0; i < K; ++i) {
        getline(cin, instructions[i]);
    }

    bool foundNonFaulty = false;
    string nonFaultySolution = "";
    bool foundFaulty = false;
    string faultySolution = "";

    for (int i = 0; i < K; ++i) {
        Cube testCube = originalCube;
        
        for (int j = 0; j < K; ++j) {
            if (i == j) continue;
            applyMove(testCube, instructions[j]);
        }

        pair<bool, bool> state = checkCubeState(testCube);

        if (state.first) {
            foundNonFaulty = true;
            nonFaultySolution = instructions[i];
            break;
        } else if (state.second) {
            foundFaulty = true;
            faultySolution = instructions[i];
        }
    }

    if (foundNonFaulty) {
        cout << nonFaultySolution << endl;
    } else if (foundFaulty) {
        cout << "Faulty" << endl;
        cout << faultySolution << endl;
    } else {
        cout << "Not Possible" << endl;
    }

    return 0;
}