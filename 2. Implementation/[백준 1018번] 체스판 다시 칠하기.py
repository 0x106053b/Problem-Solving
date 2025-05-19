N, M = map(int, input().split())
checkw = "WBWBWBWBBWBWBWBW" * 4
checkb = "BWBWBWBWWBWBWBWB" * 4

board = []
answer = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        temp = "".join(list(map(lambda x : x[j:j+8], board[i:i+8])))
        cntw, cntb = 0, 0
        for k in range(64):
            if checkw[k] != temp[k]: cntw += 1
            if checkb[k] != temp[k]: cntb += 1
        answer.append(cntw)
        answer.append(cntb)

print(min(answer))