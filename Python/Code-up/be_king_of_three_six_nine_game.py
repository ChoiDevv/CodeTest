# 3 6 9 게임의 왕이 되자

n = int(input())

for num in range(1, n + 1):
    if "3" in str(num):
        print("X" * str(num).count("3"), end=" ")
    elif "6" in str(num):
        print("X" * str(num).count("6"), end=" ")
    elif "9" in str(num):
        print("X" * str(num).count("9"), end=" ")
    else:
        print(num, end=" ")