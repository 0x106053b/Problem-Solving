from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):

            # 현재 위치(x, y)로부터 상/하/좌/우 로 1칸씩 이동한 new 위치
            nx = x + dx[i]
            ny = y + dy[i]

            # new 위치가 graph의 범위를 벗어나는 경우
            # 다른 새로운 new 위치를 탐색
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue 

            # graph 범위 안이지만 괴물이 있어 이동할 수 없는 경우
            if graph[nx][ny] == 0:
                continue

            # 이동 가능한 경로인 경우
            # 현재 노드에 적힌 숫자 + 1 하여 graph[nx][ny]까지의 최소 이동거리를 표시 (***)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 가장 오른쪽 아래 노드에 적힌 값을 반환
    return graph[N-1][M-1]


print(BFS(0,0))