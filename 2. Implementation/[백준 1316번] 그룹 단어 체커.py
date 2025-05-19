from itertools import groupby

answer = 0
for _ in range(int(input())):
    temp = ''.join(x for x, _ in groupby(input()))
    if len(temp) == len(set(temp)): answer += 1
print(answer)