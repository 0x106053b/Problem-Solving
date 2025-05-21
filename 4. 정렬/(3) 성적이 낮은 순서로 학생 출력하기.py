array = []
for _ in range(int(input())):
    name, score = input().split()
    array.append((name, int(score)))

array.sort(key=lambda x : x[1])
for x in array: print(x[0], end=" ")