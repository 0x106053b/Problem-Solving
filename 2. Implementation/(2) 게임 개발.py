N, M = map(int, input().split())
now = list(map(int, input().split()))
plan = []
for _ in range(N):
    plan.append(input().split())

# 현재 게임 캐릭터의 위치를 "2"로 표시한다.
# 현재 방문한 "0" 지역 역시 방문한 칸으로 치고 cnt = 1로 initialize한다.
plan[now[1]][now[0]] = "2"
cnt = 1

# 차례대로 방위 북 / 동 / 남 / 서의 번호에 대응하는 인덱스를 가진 이동 리스트이다.
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 사면을 다 탐색한 후에는 뒷걸음질 쳐야하기 때문에
# 사면 탐색 조건을 만족했는지를 확인하기 위해 rotate 변수를 생성한다.
rotate = [False for _ in range(4)]


while True:
    # 방향을 전환한다
    now[2] -= 1
    if now[2] < 0: now[2] = 3
    rotate[now[2]] = True

    # 방향전환 후 이동하고 싶은 위치 좌표를 저장
    ny = now[0] + dy[now[2]]
    nx = now[1] + dx[now[2]]


    # 이동하고 싶은 위치 좌표의 상태를 확인
    # (1) 이동가능한 경우
    # * rotate 리스트를 초기화해서 새로운 땅에서 사면을 모두 탐색할 수 있도록 한다.
    if plan[ny][nx] == "0":
        now[0], now[1] = ny, nx
        plan[ny][nx] = "2"
        cnt += 1
        rotate = [False for _ in range(4)]

    # (2) 이동 불가능한 경우
    else:
        # (2) - 1 사면을 모두 탐색했지만 이동할 수 있는 칸이 없는 경우
        if sum(rotate) == 4:
            ny = now[0] - dy[now[2]]
            nx = now[1] - dx[now[2]]

            # * 뒷걸음질 친 땅이 바다인경우 탐색을 종료한다.
            if plan[ny][nx] == "1":
                break

            # * 뒷걸음질 친 땅이 이미 방문한 땅일 경우("2")
            # * 이동 후 rotate 리스트를 초기화해서 새로운 땅에서 사면을 모두 탐색할 수 있도록 한다.
            else:
                plan[ny][nx] = "2"
                now[0], now[1] = ny, nx
                rotate = [False for _ in range(4)]
                continue

        else:
            continue

print(cnt)