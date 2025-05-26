import sys
K, N = map(int, input().split())
arr = []
for _ in range(K): arr.append(int(sys.stdin.readline()))

start, end = 1, max(arr)

# height(cm)로 자를 때 랜선의 개수
def lan_count(height):
    return sum(map(lambda x : x//height, arr))

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = lan_count(mid)
    if cnt < N: # 개수가 모자름 = height를 줄여야 함
        end = mid - 1
    else: # 개수가 넘침 = height를 늘릴 수 있음
        result = mid
        start = mid + 1

print(result)