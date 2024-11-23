#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>

#define ac 0xAC
#define wa 0xAD
#define pe 0xAE
#define tl 0xAF

using namespace std;

ifstream user("user.txt");
ifstream author("author.txt");
ifstream input("input.txt");


string nextToken(){
    string s;
    if(user >> s) return s;
    exit(pe);
}

long long nextLong(){
    long long n;
    if(user >> n) return n;
    exit(pe);
}

int nextInt(){
    int n;
    if(user >> n) return n;
    exit(pe);
}

int a, b;
vector<string> ans;
void read(){
    input >> a >> b;
    string s;
    while(user >> s) ans.push_back(s);
    // write code here ...
}

void write(){
    if(a > ans.size() || ans.size() > b) exit(wa);
    set<string> st;
    for(auto &s : ans){
        for(char c: s) if(c < 'a' || c > 'z') exit(wa);
        if(1 > s.size() || s.size() > 15) exit(wa);
        st.insert(s);
    }
    if(st.size() < (b + 1) / 2) exit(wa);
    exit(ac);

    // write code here ...
}

int main(){
    input.tie(nullptr)->sync_with_stdio(false);
    user.tie(nullptr)->sync_with_stdio(false);
    author.tie(nullptr)->sync_with_stdio(false);
    read();
    write();
    return 0;
}