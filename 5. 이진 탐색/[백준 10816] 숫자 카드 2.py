N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

n_dict = {}

for x in n_list:
    if x in n_dict: n_dict[x] += 1
    else: n_dict[x] = 1

keys = sorted(list(n_dict.keys()))

def binary_search(start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if keys[mid] == target:
        return n_dict[target]
    elif keys[mid] > target:
        return binary_search(start, mid-1, target)
    else:
        return binary_search(mid+1, end, target)

for x in m_list:
    print(binary_search(0, len(keys)-1, x), end=" ")