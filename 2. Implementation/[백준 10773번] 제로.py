import sys
from collections import deque

dq = deque([])

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num == 0:
        dq.pop()
    else:
        dq.append(num)

print(sum(dq))