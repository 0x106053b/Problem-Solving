# point : 2차원 list를 1차원으로 ravel하려면 => sum(list, [])

from itertools import combinations
from collections import deque

# 추가한 1벽은 'o', 전염된 2는 'x'로 표기한다.

N, M = map(int, input().split())
zeromap, graph, answer = [], [], []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph):
    queue = deque([])
    for y in range(N):
        for x in range(M):
            if graph[y][x] == '2':
                queue.append((y, x))
                while queue:
                    ay, ax = queue.popleft()
                    for i in range(4):
                        ny = ay + dy[i]
                        nx = ax + dx[i]
                        if ny < 0 or nx < 0 or ny >= N or nx >= M:
                            continue
                        elif graph[ny][nx] != '0':
                            continue
                        else:
                            graph[ny][nx] = 'x'
                            queue.append((ny, nx))                    

for y in range(N): 
    line = list(input().split())
    for x in range(M):
        if line[x] == '0': zeromap.append((y, x))
    graph.append(line)

for candidat in combinations(zeromap, 3):
    # print(candidat)
    for x in candidat: graph[x[0]][x[1]] = 'o'
    bfs(graph)
    answer.append(sum(graph, []).count("0"))
    graph = [[y.replace("o", "0").replace("x", "0") for y in x] for x in graph]

print(max(answer))