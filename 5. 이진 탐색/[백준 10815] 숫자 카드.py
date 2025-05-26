N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, input().split()))

def binary_search(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if n_list[mid] == target:
        return 1
    elif n_list[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)

for x in m_list:
    print(binary_search(x, 0, N-1), end=" ")