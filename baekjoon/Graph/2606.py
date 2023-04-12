from sys import stdin
from collections import deque
def DFS(graph, start, visited):
    visited[start] = True
    ret = str(start) + " "
    # print(str(start), end=" ")
    for i in range(len(graph[start])):
        if visited[graph[start][i]] == False:
            ret += DFS(graph, graph[start][i], visited)
    return ret

def BFS(graph):
    answer = 0
    visited = [False for _ in range(len(graph))]
    queue = deque([1])
    visited[1] = True
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    for i in visited:
        if i == True:
            answer += 1
    return answer
            

    pass
if __name__ == "__main__":
    n = int(input().rstrip())
    #bfs
    # graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    #dfs
    graph = [[]for _ in range(n+1)]
    visited = [False for _ in range(len(graph))]
    m = int(input().rstrip())

    # for i in range(m):
    #     x,y = map(int, stdin.readline().split())
    #     graph[x].append(y)
    #     graph[y].append(x)
    for i in range(m):
        x,y = map(int, stdin.readline().split())
        graph[x] += [y]
        graph[y] += [x]
    from pprint import pprint
    pprint(graph)
    ret = BFS(graph)
    print(ret-1)
    # ret = DFS(graph, 1, visited)
    # arr = ret.split()
    # print(len(arr)-1)
