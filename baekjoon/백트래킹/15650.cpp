#include <iostream>
#define MAX 9

int n, m, count = 0;
int arr[MAX] = {0,};
std::string values[MAX*MAX] = {0,};
bool visited[MAX] = {0,};
void dfs(int cnt){
    if (cnt == m){
        std::string value;
        int check_duplicate = 0;
        if (values[count].length() > 0){
            for (int i = 1; i <= m; i++){
                for(int j = 0; j < m; j++){
                    if (arr[i] == values[count][j])
                        check_duplicate++;
                }
            }
        }
        if (check_duplicate == m)
            return;

        for (int i = 0; i < m; i++){
            std::cout << arr[i] << ' ';
            value += arr[i];
        }
        count++;  
        values[count] = value;      
        std::cout << std::endl;
        return;
    }
    //how to reset??
    for (int i = 1; i <= n; i++){
        if (!visited[i]){
            visited[i] = true;
            arr[cnt] = i;
            dfs(cnt + 1);
            visited[i] = false;
        }
    }
}

int main(){
    std::cout << values[count].length() << std::endl;

    std::cin >> n >> m;
    dfs(0);
    return 0;
}