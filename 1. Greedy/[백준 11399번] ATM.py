N = int(input())
lst = sorted(list(map(int, input().split())))
result = 0
for idx, x in enumerate(lst):
    result += (len(lst) - idx)*x

print(result)