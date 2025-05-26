import sys
import heapq

arr = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(arr) == 0: print(0)
        else:
            y = heapq.heappop(arr)
            print(y[1])
    else:
        heapq.heappush(arr, (-x, x))