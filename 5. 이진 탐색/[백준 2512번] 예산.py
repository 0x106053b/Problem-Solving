N = int(input()) # 지방의 수
arr = list(map(int, input().split())) # 지방의 요청 예산 array
M = int(input()) # 총 예산

start, end = 1, max(arr)

# arr element > amount(배정 예산 한도) 라면, amount만큼만 배정받고
# arr element < amount(배정 예산 한도) 라면, 요청한만큼만 배정
def yesan_sum(amount):
    return sum(map(lambda x : min(x, amount), arr))

result = 0
while start <= end:
    mid = (start + end) // 2
    temp = yesan_sum(mid)
    if temp > M: # 예산 초과 = mid를 줄여야함
        end = mid - 1
    else: # 예산 남음 = mid를 늘려도 됨
        result = mid
        start = mid + 1

print(result)