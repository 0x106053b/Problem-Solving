N, M, K = map(int, input().split())
num = sorted(list(map(int, input().split())))

a = M // (K + 1)
b = M % (K + 1)

print(a*((K * num[-1]) + num[-2]) + (b * num[-1]))