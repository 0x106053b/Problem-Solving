N = int(input())
a , b = N//5, N % 5

while (a > 0):
    if b % 3 != 0: # 5로 나눈 나머지(b)가 3의 배수가 아니라면
        a -= 1 # a를 깎아서
        b += 5 # b에게 나눠준다
    else: # 5로 나눈 나머지(b)가 3의 배수라면
        break

if b % 3 != 0: print(-1)
else: print(a+(b//3))