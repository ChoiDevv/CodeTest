# 숫자 카드 게임

M, N = map(int, input().split())
input_max_list = []

for i in range(M):
    input_max_list.append(min(list(map(int, input().split()))))

print(max(input_max_list))
