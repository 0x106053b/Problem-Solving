from collections import deque
import sys
import itertools

M, N = map(int, input().split())
graph = []
tomato1 = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
    for j in range(M):
        if temp[j] == 1: tomato1.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque(tomato1)

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            dq.append((nx, ny))

    
graph = list(itertools.chain.from_iterable(graph))

if all(graph): print(max(graph)-1)
else: print(-1)
