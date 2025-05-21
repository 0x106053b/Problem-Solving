import sys
N = int(input())
MAX_NUM = 1000000
array = [False for _ in range(2*MAX_NUM+1)]
for _ in range(N):
    array[int(sys.stdin.readline()) + MAX_NUM] = True

for x in range(len(array)):
    for _ in range(array[x]): print(x-MAX_NUM)