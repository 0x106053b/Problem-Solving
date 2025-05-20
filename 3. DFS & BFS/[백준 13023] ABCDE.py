import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
answer = 0

def dfs(x, depth):
    global answer
    if depth == 4:
        answer = 1
        return
    for y in graph[x]:
        if not visited[y]: 
            visited[y] = True # dfs 탐색 전에 visited = True 처리하기
            dfs(y, depth+1)
            visited[y] = False # 만약에 depth = 4 도달하지 못해서 그냥 backtracking 되는 경우, visited를 해제해준다.

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(N):
    visited = [False for _ in range(N)]
    visited[x] = True # dfs 탐색 전에 visited = True 처리하기
    dfs(x, 0)
    if answer == 1:
        break

print(answer)