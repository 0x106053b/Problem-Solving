N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)

def tree_sum(height):
    return sum(map(lambda x : max(x-height, 0), arr))

while start <= end:
    mid = (start + end) // 2
    tree = tree_sum(mid)
    if tree < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)