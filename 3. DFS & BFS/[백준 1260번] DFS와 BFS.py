from collections import deque

N, M, V = map(int, input().split())

# 전략 : graph의 index와 노드의 번호를 일치시키기 위해
# 그 어떤 노드와도 연결되지 않은 가상의 빈 노드 0번을 상정한다.
graph = [[] for _ in range(N+1)]
dfs_visited = [False for _ in range(N+1)]
bfs_visited = [False for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(x):
    # 현재 노드를 방문 처리
    dfs_visited[x] = True
    print(x, end=" ")

    # 현재 노드의 인접 노드 탐색
    # 노드 번호가 가장 적은 것부터 정렬될 수 있도록 sort한다.
    # x번 노드는 이미 방문처리 되었으므로 graph[x]에 대해 여러번 sort하지 않는다.
    for v in sorted(graph[x]):
        # 인접 노드가 방문처리 되지 않았다면 해당 노드에 대해 DFS
        if not dfs_visited[v]:
            DFS(v)

def BFS(x):
    
    # initialize deque
    dq = deque([x])
    bfs_visited[x] = True
    print(x, end=" ")

    # BFS큐에 담긴 노드가 하나도 없을 떄까지 반복한다.
    while dq:
        v = dq.popleft()

        # popleft한 v노드의 인접노드(nv)를 모두 탐색하면서
        # 아직 방문하지 않은 노드라면 모두 큐에 삽입
        for nv in sorted(graph[v]):
            if not bfs_visited[nv]:
                dq.append(nv)
                bfs_visited[nv] = True
                print(nv, end=" ")

DFS(V)
print()
BFS(V)