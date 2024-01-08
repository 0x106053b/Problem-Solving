N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_visited = [False for _ in range(N+1)]
bfs_visited = [False for _ in range(N+1)]

def DFS(x):
    dfs_visited[x] = True
    for v in graph[x]:
        if not dfs_visited[v]:
            DFS(v)


def BFS(x):
    from collections import deque
    dq = deque([x])
    bfs_visited[x] = True

    while dq:
        v = dq.popleft()
        for nv in graph[v]:
            if not bfs_visited[nv]:
                dq.append(nv)
                bfs_visited[nv] = True

# DFS로 구현
DFS(1)
print(sum(dfs_visited)-1)

# BFS로 구현    
# BFS(1)
# print(sum(bfs_visited)-1)