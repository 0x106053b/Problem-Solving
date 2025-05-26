# strategy : n_list, m_list를 모두 내장 sort 사용하여 정렬한 후 (O(nlogn))
# 두 리스트를 앞에서부터 탐색하면서 있/없 체크하기

# (idea #1) 이분탐색하여 있/없 체크하기
# (idea #2) set(n_list) 하고 for문 돌려서 있/없 체크하기 

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = [(idx, int(x)) for idx, x in enumerate(input().split())]

n_list.sort()
m_list = sorted(m_list, key=lambda x : x[1])

n_idx = 0

for m_idx, m in enumerate(m_list):
    while n_idx < N - 1 and n_list[n_idx] < m[1]: # 더 뒤로 이동할 수 있는 n_list element가 있는 경우
        n_idx += 1
    if n_list[n_idx] == m[1]:
        m_list[m_idx] = (m_list[m_idx][0], '1')
    else:
        m_list[m_idx] = (m_list[m_idx][0], '0')

print('\n'.join(list(map(lambda x : x[1], sorted(m_list, key=lambda x : x[0])))))