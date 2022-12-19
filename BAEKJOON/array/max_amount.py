# 최댓값

n = 9
num_list = []

for i in range(n):
    input_number = int(input())
    num_list.append(input_number)

print(max(num_list))
print(num_list.index(max(num_list)) + 1)