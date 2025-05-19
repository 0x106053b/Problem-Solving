# point : 2차원 list element 값 기준으로 정렬 시, tuple로 묶으면 다중 key 정렬 가능.
# 정렬 방향 다르게 하고 싶다면 lambda x : (-x[0], x[1]) 이런식으로 하면됨~

import sys

numbers = []
N = int(input())
for _ in range(N): numbers.append(int(sys.stdin.readline()))
numbers.sort()

print(round(sum(numbers)/N))
print(numbers[N//2])

freq_dict = {}
for x in numbers:
    if x in freq_dict.keys(): freq_dict[x] += 1
    else: freq_dict[x] = 1

freq_dict = sorted(freq_dict.items(), key = lambda x : (-x[1], x[0]))

if len(freq_dict) > 1 and freq_dict[0][1] == freq_dict[1][1]: print(freq_dict[1][0])
else: print(freq_dict[0][0])

print(numbers[-1]-numbers[0])