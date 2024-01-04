N = int(input())
now = [1, 1]

for x in list(input().split()):
    if (x == "U") & (now[0] >= 2): # UP 명령 + 위로 이동할 칸이 있는 경우
        now[0] -= 1
    elif (x == "R") & (now[1] <= 4): # RIGHT 명령 + 오른쪽으로 이동할 칸이 있는 경우
        now[1] += 1
    elif (x == "D") & (now[0] <= 4): # DOWN 명령 + 아래로 이동할 칸이 있는 경우
        now[0] += 1
    elif (x == "L") & (now[1] >= 2): # LEFT 명령 + 왼쪽으로 이동할 칸이 있는 경우
        now[1] -= 1

print(now[0], now[1])