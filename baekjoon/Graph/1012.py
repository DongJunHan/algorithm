from collections import deque
from sys import stdin

answer = 0
def DFS(graph, visited, queue):
    global answer
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x, y = queue.popleft()
        answer += 1
        for i in range(4):
            xm = x + dx[i]
            ym = y + dy[i]
            if 0 <= xm < len(graph) and 0 <= ym < len(graph[0]) and visited[xm][ym] == False and graph[xm][ym] == 1:
                visited[xm][ym] = True
                queue.append((xm,ym))
                DFS(graph, visited, queue)

if __name__ == "__main__":
    T = int(stdin.readline().rstrip())
    graph_arr = []
    visited_arr = []
    for i in range(T):
        M, N, K = stdin.readline().rstrip().split()
        graph = [[0] * int(M) for _ in range(int(N))]
        visited = [[False] * int(M) for _ in range(int(N))]
        for i in range(int(K)):
            x, y = map(int, stdin.readline().split())
            graph[y][x] = 1
        graph_arr.append(graph)
        visited_arr.append(visited)
    
    for k in range(T):
        arr = []
        graph = graph_arr[k]
        visited = visited_arr[k]
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if visited[i][j] == False and graph[i][j] == 1:
                    queue = deque()
                    queue.append((i,j))
                    visited[i][j] = True
                    DFS(graph, visited, queue)
                    arr.append(answer)
                    answer = 0
        print(len(arr))


