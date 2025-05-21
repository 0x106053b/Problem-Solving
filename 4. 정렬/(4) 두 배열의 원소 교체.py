N, K = map(int, input().split())
array1 = sorted(list(map(int, input().split())))
array2 = sorted(list(map(int, input().split())), reverse=True)
answer = 0
for i in range(K): 
    answer += max(array1[i], array2[i])
answer += sum(array1[K:])
print(answer)