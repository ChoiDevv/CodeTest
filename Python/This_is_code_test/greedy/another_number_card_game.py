# 숫자 카드 게임

n, m = map(int, input().split())
result = 0

for i in range(n):
    array = list(map(int, input().split()))
    result = max(result, min(array))

print(result)
