N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr, key=lambda x : abs(x))

sum_arr = [(arr[i] + arr[i+1], i) for i in range(0, N-1)]
sum_arr = sorted(sum_arr, key=lambda x : abs(x[0]))
idx = sum_arr[0][1]

result = sorted(arr[idx:idx+2])
print(result[0], result[1])