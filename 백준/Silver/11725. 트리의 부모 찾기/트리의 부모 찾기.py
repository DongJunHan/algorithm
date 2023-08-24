import sys
sys.setrecursionlimit(10**6)
def make_tree(arrs, a, visited):
    for i in arrs[a]:
        if visited[i] == None:
            visited[i] = a
            make_tree(arrs, i, visited)

if __name__ == "__main__":
    N = int(input())
    visited = [None for _ in range(N+1)]
    arr = [[] for _ in range(N+1)]
    for _ in range(N-1):
        one, second = map(int, sys.stdin.readline().strip().split())
        arr[one].append(second)
        arr[second].append(one)
    make_tree(arr,1,visited)
    for i in range(2, N+1):
        print(visited[i])
    