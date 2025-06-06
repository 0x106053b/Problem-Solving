import sys
arr, result = [], []
for _ in range(int(input())): 
    arr.append(tuple(map(int, sys.stdin.readline().split())))
arr = sorted(arr, key=lambda x : (x[0], x[1]))

for x in arr:
    if len(result) == 0 or result[-1][1] <= x[0]:
        result.append(x)
        continue
    for y in result:
        if y[0] <= x[0] and x[1] <= y[1]:
            result.remove(y)
            result.append(x)
            break

print(len(result))