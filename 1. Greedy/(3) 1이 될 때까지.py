N, K = map(int, input().split())

# [ 전략 ]
# K 값과 상관 없이 N에서 1을 뺴는 것 보다 N을 K로 나누는 것이 전체 연산 횟수를 줄이는 데 유리하다.

cnt = 0 
while True:
    if N == 1:
        break
    if N % K == 0: # K로 나누기를 우선적으로
        N = int(N//K)
    else:
        N = N - 1
    cnt += 1
print(cnt)