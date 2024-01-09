from collections import deque

N, K = map(int, input().split())
dq = deque([N])

# visited 배열은 N에서 배열의 각 인덱스 번호까지의 최소 이동거리를 의미한다.
visited = [-1 for _ in range(100001)]

# N에서 N까지의 이동거리 0칸 (깊이 0)
visited[N] = 0

while True:
    x = dq.popleft()

    if x == K:
        break

    next_step = [x-1, x+1, 2*x]
    for next in next_step:

        # 다음 이동이 범위 밖이라면 pass
        if next < 0:
            continue

        # next가 visited 배열의 범위를 초과할 수 있다.
        # 그러나 visited 배열의 범위를 초과한 이동에 대한 정보는 필요 없으므로
        # try-except 문으로 묶어 해당 오류에 대해 넘어갈 수 있도록 핸들링한다.
        try:
            if visited[next] < 0 :
                visited[next] = visited[x] + 1
                dq.append(next)
        except:
            continue

print(visited[K])