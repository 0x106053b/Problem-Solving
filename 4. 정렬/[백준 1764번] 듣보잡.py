import sys

N, M = map(int, sys.stdin.readline().split())
arr1 = sorted([sys.stdin.readline() for _ in range(N)])
arr2 = sorted([sys.stdin.readline() for _ in range(M)])
result = []
index1 = index2 = 0

while index1 < len(arr1) and index2 < len(arr2):
    if arr1[index1] == arr2[index2]: 
        result.append(arr1[index1])
        index1 += 1
        index2 += 1
    elif arr1[index1] < arr2[index2]:
        index1 += 1
    else:
        index2 += 1

print(len(result))
print("\n".join(result))