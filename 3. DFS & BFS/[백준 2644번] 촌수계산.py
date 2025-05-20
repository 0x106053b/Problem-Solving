def dfs(x, depth):
    if visited[x] >= 0: return
    else:
        visited[x] = depth
        for k in graph[x]:
            dfs(k, depth+1)

n = int(input())
visited = [-1 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
a, b = map(int, input().split())
for _ in range(int(input())):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

dfs(a, 0)
print(visited[b])