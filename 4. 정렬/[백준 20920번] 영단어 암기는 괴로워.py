# 자주 나오는 단어일수록 앞에 배치
# 단어가 길수록 앞에 배치
# 알파벳 사전순 배치
# (+) 길이가 M이상인 단어들만 기록

import sys

N, M = map(int, input().split())
arr = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in arr.keys():
            arr[word][0]  += 1
        else:
            arr[word] = [1, len(word)]

sorted_arr = sorted(list(arr.items()), key=lambda x : (-x[1][0], -x[1][1], x[1][2]))
print("\n".join(list(map(lambda x : x[0], sorted_arr))))
