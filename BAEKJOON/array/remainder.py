# 나머지

n = 10
input_list = []

for i in range(n):
    input_number = int(input())
    input_list.append(input_number)

print(len(set(list(map(lambda num: num % 42, input_list)))))