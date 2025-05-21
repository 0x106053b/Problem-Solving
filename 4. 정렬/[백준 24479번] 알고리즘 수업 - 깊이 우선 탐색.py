import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
step = 1

def dfs(x):
    global step
    visited[x] = step
    for y in sorted(graph[x]):
        if not visited[y]:
            step += 1
            dfs(y)

dfs(R)
for x in visited[1:]: print(x)