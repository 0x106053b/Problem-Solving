N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
cnt = 0

def DFS(x):
    for v in graph[x]:
        if not visited[v]:
            visited[v] = True
            DFS(v)

for i in range(1, N+1):
    if not visited[i]: 
        DFS(i)
        cnt += 1

print(cnt)