from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

danji = []

def BFS(x, y):
    cnt = 0
    dq = deque([])
    dq.append((x, y))
    graph[x][y] = -1 # graph[x][y] = -1 이라는 것은 (x, y)를 방문했다는 것

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                cnt += 1
                dq.append((nx, ny))

    return cnt

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            danji.append(BFS(i, j)+1)

danji.sort()
print(len(danji))
print("\n".join(map(str, danji)))