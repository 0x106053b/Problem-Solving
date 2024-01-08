N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def DFS(x, y): # 세로 이동 x / 가로 이동 y
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    
    if graph[x][y] == 0: # 아직 방문하지 않은 얼음 노드
        graph[x][y] = 1 # 방문처리

        # 상/하/좌/우 노드를 방문 (탐색 가능한 모든 노드 확인)
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        return True # 발견한 얼음 한칸을 시작으로 주변 얼음 다 탐색한 후 return True (아이스크램 1개)
    
    return False # 방문은 했는데 얼음이 아닌 경우 return False
    
cnt = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j): cnt += 1 # initial start (i, j)에서 시작해 얼음덩어리를 하나 발견한 경우

print(cnt)