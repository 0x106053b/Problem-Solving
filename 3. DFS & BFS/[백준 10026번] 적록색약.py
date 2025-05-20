from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, graph, rgb):
    if y < 0 or x < 0 or y >= N or x >= N:
        return False
    elif graph[y][x] != rgb:
        return False
    else:
        graph[y][x] = None
        for i in range(4):
            dfs(y+dy[i], x+dx[i], graph, rgb)

N = int(input())
answer1, answer2 = 0, 0
graph1 = []

for _ in range(N): graph1.append(list(input()))
graph2 = deepcopy(graph1)
graph2 = [[b.replace("R", "G") for b in a] for a in graph2]

for y in range(N):
    for x in range(N):
        rgb1, rgb2 = graph1[y][x], graph2[y][x]
        if rgb1 is not None:
            answer1 += 1
            dfs(y, x, graph1, rgb1)
        if rgb2 is not None:
            answer2 += 1
            dfs(y, x, graph2, rgb2)

print(answer1, answer2)