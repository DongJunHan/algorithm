from sys import stdin
from collections import deque
def BFS(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    ret = str(start)+' '
    while len(queue) > 0:
        cur_node = queue.popleft()
        for i, v in enumerate(graph[cur_node]):
            if v == 1 and visited[i] == False:
                visited[i] = True
                ret = ret + str(i) + ' '
                queue.append(i)

    return ret.rstrip()

def DFS(graph, start, visited):
    visited[start] = True
    print(str(start), end=" ")
    for i in range(1,len(graph)):
        if visited[i] == False and graph[start][i] == 1:
            ret = DFS(graph, i, visited)
    


if __name__ == "__main__":
    a = input().strip()
    arr = a.split()
    graph:list = [[0] * (int(arr[0]) + 1) for _ in range(int(arr[0]) + 1)]

    # graph = {}
    #make graph
    for i in range(int(arr[1])):
        a, b = map(int, stdin.readline().split())
        graph[a][b] = graph[b][a] = 1
    from pprint import pprint

    print(graph)
    visited = [False] * len(graph)
    DFS(graph, int(arr[2]), visited)
    print("")
    print(BFS(graph, int(arr[2])))