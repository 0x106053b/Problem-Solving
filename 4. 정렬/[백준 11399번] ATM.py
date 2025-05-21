N = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
print(sum([arr[i] * (i+1) for i in range(len(arr))]))