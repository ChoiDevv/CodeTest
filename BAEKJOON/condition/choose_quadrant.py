# 사분면 고르기

n = int(input())
m = int(input())

if n > 0:
    print(1 if m > 0 else 4)
else:
    print(2 if m > 0 else 3)