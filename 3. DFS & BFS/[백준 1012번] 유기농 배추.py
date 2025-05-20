# point : python은 default recusion 깊이가 매우 얕으므로, recursion error가 발생한다면 (RuntimeError)
# import sys + sys.setrecursionlimit(10 ** 6) 이런식으로 재귀의 깊이를 깊게 설정해준다.

import sys 
sys.setrecursionlimit(10000)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x):
    graph[y][x] = 2
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        elif graph[ny][nx] != 1:
            continue
        else:
            dfs(ny, nx)


for _ in range(int(input())):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                cnt += 1
                dfs(y, x)
    
    print(cnt)