#include <iostream>
#define MAX 9
using namespace std;

int n,m;
int arr[MAX] = {0,};
bool visited[MAX] = {0,};
/*
    1. 재귀를 활용하여 깊이우선탐색을 해야함.
    2. 탐색여부를 확인해서 체크하는 변수를 선언해야함.
    * 백트래킹 방식은 아니다. 왜냐면 백트래킹 방식은 이렇게 재귀를 사용하여 탐색을 하다가도 아닌거같으면 돌아옴.
*/
void dfs(int cnt){
    if (cnt == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << ' ';
        }
        cout << endl;
        return;
    }
    for(int i = 1; i <= n; i++){
        if(!visited[i]){
            visited[i] = true;
            arr[cnt] = i;
            dfs(cnt+1);
            visited[i] = false;
        }
    }
}

int main(){
    cin >> n >> m;
    dfs(0);
}