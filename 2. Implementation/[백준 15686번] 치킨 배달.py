from itertools import combinations

N, M = map(int, input().split())
home, chicken = [], []

# 집과 치킨집 정보를 입력받는대로 튜플 형태로 저장한다.
for i in range(N):
    row = input().split()
    for j in range(N):
        if row[j] == "1": home.append((i, j))
        elif row[j] == "2" : chicken.append((i, j))

# 모든 집-치킨집 사이의 거리를 계산한 치킨거리 행렬을 생성한다.
chick_dist = []
for c in chicken:
    dist = list(map(lambda x : abs(x[0]-c[0]) + abs(x[1]-c[1]), home))
    chick_dist.append((dist))

# 치킨거리 행렬의 행 번호(치킨집) 중 M개를 뽑는 조합을 생성한다.
# chick_dist 자체를 combination하지 않은 이유는 메모리 절약을 위해서이다.
comb = combinations(range(len(chick_dist)), M)
result_lst = []


for c in comb:
    result = 0
    temp = list(map(lambda x : chick_dist[x], c))
    for i in range(len(home)):
        
        # 선택된 조합 내에서의 치킨거리의 합을 구해 result에 저장한다.
        result += min(list(zip(*temp))[i])
    result_lst.append(result)

print(min(result_lst))