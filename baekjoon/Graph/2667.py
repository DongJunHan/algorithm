from collections import deque
from sys import stdin

visited = []
answer = 0

def solution(graph, visited, stack):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    global answer
    while stack:
        x,y = stack.popleft()
        answer += 1
        for i in range(4):
            xm = x + dx[i]
            ym = y + dy[i]
            if 0 <= xm < len(graph) and 0 <= ym < len(graph[0]) and visited[xm][ym] == False and graph[xm][ym] == 1:
                visited[xm][ym] = True
                stack.append((xm , ym))
                solution(graph, visited, stack)

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    visited = [[False for _ in range(n)]for _ in range(n)]
    graph = []
    for i in range(n):
        graph.append(list(map(int, stdin.readline().rstrip())))
    # from pprint import pprint
    # pprint(graph)
    arr = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if visited[i][j] == False and graph[i][j] == 1:
                stack = deque()
                stack.append((i,j))
                visited[i][j] = True
                solution(graph, visited, stack)
                arr.append(answer)
                answer = 0
    print(len(arr))
    arr.sort()
    for i in arr:
        print(i)