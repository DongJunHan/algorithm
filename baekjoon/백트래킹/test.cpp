#include <iostream>
#define MAX 9

int n, m, count = 0;
int arr[MAX] = {0,};
bool visited[MAX] = {0,};
void dfs(int cnt){
    if (cnt == m){
        count++;
        for (int i = 0; i < m; i++){
            std::cout << arr[i] << ' ';
        }
        std::cout << std::endl;
        return;
    }
    for (int i = 1; i <= n; i++){
        if (!visited[i]){
            visited[i] = true;
            arr[cnt] = i;
            dfs(cnt+1);
            visited[i] = false;
        }
    }
}

int main(){
    std::cin >> n >> m;
    dfs(0);
    std::cout << count << std::endl;
    return 0;
}