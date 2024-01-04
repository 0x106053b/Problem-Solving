now = input()
move_list = [(+2, +1), (+2, -1), (-2, +1), (-2, -1), 
        (+1, -2), (+1, +2), (-1, -2), (-1, +2)]

cnt = 0
for move in move_list:
    nx = ord(now[0])-96 + move[0]
    ny = int(now[1]) + move[1]
    if nx < 1 or nx > 8 or ny < 1 or nx > 8:
        continue
    else:
        cnt += 1

print(cnt)