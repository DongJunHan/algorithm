from collections import deque
def BFS(graph, start):
    visited = {i:False for i in graph.keys()}
    # queue = [start]
    queue = deque([start])
    print(queue)
    visited[start] = True
    result = str(start)
    while len(queue) > 0:
        current = queue.popleft()
        for nxt in graph[current]:
            if not visited[nxt]:
                queue.append(nxt)
                print(f"queue : {queue}")
                visited[nxt] = True
                result += str(nxt)
    return result, visited


if __name__ == "__main__":
    graph = {2:[4,3], 3:[5,7], 4:[8,9], 8:[],9:[], 5:[],7:[]}
    start = 2
    ret, visited = BFS(graph, start)
    print(ret)
