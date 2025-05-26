# 백준 1920번 수 찾기 문제를 이진 탐색으로 구현하기.

def binary_search(target, start, end):
    if start > end: return 0
    mid = (start + end) // 2
    if n_list[mid] == target:
        return 1
    elif n_list[mid] < target:
        return binary_search(target, mid+1, end)
    else:
        return binary_search(target, start, mid-1)

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for x in m_list:
    print(binary_search(x, 0, N-1))