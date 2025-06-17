from decimal import Decimal

X, Y = map(int, input().split()) # X : 여태까지 한 게임의 수 / Y : 여태까지 승리한 게임의 수
rate = int((Decimal(Y)/Decimal(X))*100)
start, end = 1, 1000000000
result = []

while start <= end:
    mid = (start + end) // 2
    Z = int(Decimal(Y+mid)/Decimal(X+mid)*100)
    # print(f"start : {start} / end : {end} / mid : {mid} / Z : {Z} / int((Y/X)*100) : {int((Y/X)*100)}")
    if Z == rate: # (1) mid번 게임을 추가 플레이해도 변동 X
        start = mid + 1
    else: # (2) mid번 추가 플레이한 결과 승률 변동
        end = mid - 1 # '최소' 추가 플레이 수가 문제 조건이므로 end의 range를 하향
        result.append(mid)

result = sorted(result)
if len(result): print(result[0])
else: print(-1)