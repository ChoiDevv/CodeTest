# 큰 수의 법칙

N, M, K = map(int, input().split())  # N - 배열의 크기, M - 숫자가 더해지는 횟수
input_list = list(map(int, input().split()))
answer = 0
count = 0

input_list = sorted(input_list, reverse=True)

for i in range(M):
    if count < K:
        answer += input_list[0]
        count += 1
    else:
        answer += input_list[1]
        count = 0

print(answer)