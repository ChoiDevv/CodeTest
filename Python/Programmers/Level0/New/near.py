# 가까운 수

def solution(array, n):
    answer = 0

    # [10, 11, 12, 14], 13일 때
    # 13 - 12 = 1 13 - 14 = -1이면 14가 더 가까워진 거처럼 보이지만 이는 오류
    # 절대값으로 변경하면 13 - 12 = 1 13 - 14 = 1 이 되므로 12와 14를 저장해준다. 다만 여기서 또 변경되면 리스트를 비우고 저장해야된다.
    # 더 좋은 방법은 없을까?

    return anwer


def change(n):
    if n < 0:
        return -n
    return n

array = [10, 11, 12, 14]
answer = []
n = 13
test = [change(n - num) for num in array]
# [3, 2, 1, 1]

for i in range(1, len(test)):
    if test[i] == min(test):
        answer.append(array[i])

print(answer)