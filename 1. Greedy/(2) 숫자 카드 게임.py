N, M = map(int, input().split())
card = []
for i in range(N):
    card.append(min(map(int, input().split()))) # 매 행을 입력받을 때마다 해당 행에서 가장 작은 값을 card(list)에 append
print(max(card)) # card(list)에서 가장 큰 값을 출력