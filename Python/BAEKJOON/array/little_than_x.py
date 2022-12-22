# x보다 작은 수

N, X = map(int, input().split())
num_list = list(map(int, input().split()))
answer = list(filter(lambda n: n < X, num_list))

for num in answer:
    print(num, end = " ")