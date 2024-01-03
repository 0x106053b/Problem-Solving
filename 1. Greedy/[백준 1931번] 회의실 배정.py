N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=lambda x : (x[1], x[0]))
# (1) 회의 종료 시각을 기준으로 오름차순 정렬
# (2) 회의 시작 시각을 기준으로 오름차순 정렬

# [ 전략 ]
# 어떤 회의의 종료 시점 기준으로 더 많은 회의를 배정하려면
# 시작 시간이 현재 시점 이후이면서 + 종료 시점이 현재와 가장 가까운 (길이가 짧은) 회의를 배정해야 함.


end = lst[0][1]
# 종료 시각을 기준으로 오름차순 정렬한 회의 중 맨 첫 번째 회의의 종료시각

cnt = 1
# lst[0] 회의를 자동적으로 배정하게 되므로 cnt = 1 부터 시작한다.

for i in range(1, len(lst)):
    if lst[i][0] >= end:
        end = lst[i][1]
        cnt += 1
        
print(cnt)