N, K = map(int, input().split())
lst = [(x+1) for x in range(N)]
result = []
idx = 0

# 원형 테이블이기 때문에 일정 index를 초과하는 경우 테이블에 앉은 사람 수로 index를 나누어
# index가 순환할 수 있도록 구현
while lst:
    idx = (idx + K - 1)%len(lst)
    result.append(lst[idx])
    lst.remove(lst[idx])

result = list(map(str, result))
print(f"<{', '.join(result)}>")