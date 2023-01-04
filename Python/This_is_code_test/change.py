# Greedy 3-1. 거스름돈

# 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 알고리즘 개념이다.

def change(n):
    change_list = [500, 100, 50, 10]
    count = 0

    for coin in change_list:
        count += n // coin
        n %= coin

    return count

print(change(1260))