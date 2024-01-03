import sys

# heapq 를 이용한 우선순위 큐로 구현하는 것이 전략이다.
import heapq

card = []

# 각 카드묶음의 장수를 입력받는다.
# 이 때 최대 입력 길이(N)가 100,000이기 때문에 sys.stdin.readline()을 이용하여 빠르게 입력받을 수 있도록 한다.
# 입력받는대로 card라는 리스트에 우선순위 큐 형태로 값이 입력된다. (자동정렬)
for _ in range(int(input())):
    heapq.heappush(card, int(sys.stdin.readline()))

result = 0

# 모든 카드 묶음이 더해질 때까지(len(card) == 1) 합산한다.
# 최소 힙이기 때문에 연속해서 두 개의 노드를 heappop()하면 가장 적은 수의 카드, 두번째로 적은 수의 카드 묶음이 return된다.
# return된 두 카드 묶음을 더한 값을 곧바로 card 최소 힙에 다시 push한다.
while (len(card) > 1):
    two_sum = heapq.heappop(card)+heapq.heappop(card)
    result += two_sum
    heapq.heappush(card, two_sum)
print(result)