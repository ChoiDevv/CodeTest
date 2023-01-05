# 큰 수의 법칙

N, M, K = list(map(int, input().split()))

data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

count = (M // (K + 1)) * K

result = 0
result += count * first
result += (M - count) * second

print(result)