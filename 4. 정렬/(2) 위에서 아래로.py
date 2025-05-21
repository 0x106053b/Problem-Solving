array = []
for _ in range(int(input())):
    array.append(int(input()))

array.sort(reverse=True)
for x in array: print(x, end= " ")