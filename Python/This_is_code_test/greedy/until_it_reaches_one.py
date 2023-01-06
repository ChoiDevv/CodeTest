# 1이 될 때까지

m, k = map(int, input().split())
count = 0

while True:
    if m == 1:
        break
    if m % k == 0:
        m = m // k
    else:
        m -= 1
    count += 1

print(count)