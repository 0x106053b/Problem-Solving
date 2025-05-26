# point : 힙 자료구조. heappush 할때마다 자료구조가 오름차순으로 정렬된다.
# strategy : lecture에 2차원 리스트로 강의 스케줄 입력 > sorted로 시작시간 & 종료시간 순 오름차순 정렬
# *모든 lecture에 강의실을 배정해야 하기에* result를 heap 자료구조로 하여 강의실 배정.

import sys
import heapq

N = int(input())
lecture = []
result = []
for _ in range(N):
    lecture.append(list(map(int, sys.stdin.readline().split())))
lecture = sorted(lecture, key=lambda x : (x[0], x[1]))

# result의 각 element는 element_idx 번째 회의실의 회의 종료 시각
heapq.heappush(result, lecture[0][1])

for i in range(1, N):
    if result[0] <= lecture[i][0]: # 스케줄된 회의 중 종료시간이 가장 이른 회의실에 배정 가능한 경우
        heapq.heappop(result)
        heapq.heappush(result, lecture[i][1]) # 회의실 종료시간 업데이트
    else:
        heapq.heappush(result, lecture[i][1]) # 새로운 회의실 배정

print(len(result))