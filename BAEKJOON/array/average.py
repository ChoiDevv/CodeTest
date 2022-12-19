# 평균

n = int(input())
input_list = sorted(list(map(int, input().split())))[::-1]
answer = []

for num in input_list:
    answer.append(num / max(input_list) * 100)
    
print(sum(answer) / n)