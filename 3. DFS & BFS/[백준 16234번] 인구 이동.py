from collections import deque
import sys
import math

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, L, R = map(int, sys.stdin.readline().split())
A = []
answer = 0
for _ in range(N): A.append(list(map(int, sys.stdin.readline().split())))

def bfs(r, c, moved):
    global visited
    global A
    visited[r][c] = True 
    queue = deque([(r, c)])
    yh = [A[r][c]]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N: # 인접한 국가의 범위 내 여부 확인
                continue
            elif visited[ny][nx]: # 이미 어떤 연합에 들어왔는지 여부 확인 (True / False / 어떤 정수)
                continue
            elif abs(A[y][x] - A[ny][nx]) < L or abs(A[y][x] - A[ny][nx]) > R: # 인구수가 L이상 R이하인지 확인
                continue
            else:
                yh.append(A[ny][nx])
                queue.append((ny, nx))
                visited[ny][nx] = True

    # visited에서 True인 것 (현재 연합에서 count 완료된 셀) 을 평균처리해서 정수로 때우기
    average = math.floor(sum(yh)/len(yh))

    # A 수정하기
    for i in range(N):
        for j in range(N):
            if visited[i][j] is True:
                visited[i][j] = "x"
                A[i][j] = average

    if len(yh) > 1: moved = True
    return moved
            
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    moved = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                moved = bfs(r, c, moved)
    if not moved:
        break
    else:
        answer += 1

print(answer)