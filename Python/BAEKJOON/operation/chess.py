# 킹, 퀸, 룩, 비숍, 나이트, 폰

input_list = list(map(int, input().split()))
chess_list = [1, 1, 2, 2, 2, 8]

for i in range(len(input_list)):
    chess_list[i] = chess_list[i] - input_list[i]

for num in chess_list:
    print(num, end = " ")