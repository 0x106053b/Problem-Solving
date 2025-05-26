# strategy : 절댓값 오름차순으로 정렬했을 때, 뒤에 오는 값과의 합이 최소화되는 조합.
# => 두 값의 절댓값 차이가 가장 작으면서 + 부호가 서로 다른 숫자의 합이 정답이 될 가능성이 높다

N = int(input())
num = map(int, input().split())
num = sorted(num, key=lambda x : abs(x))
combinations = [abs(num[idx] + num[idx+1]) for idx in range(N-1)]
index = combinations.index(min(combinations))
for x in sorted(num[index:index+2]): print(x, end= " ")