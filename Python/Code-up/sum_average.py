# 정수 3개 입력받아 합과 평균 출력하기

num1, num2, num3 = map(int, input().split())

print("{0} {1:.2f}".format(num1 + num2 + num3, (num1 + num2 + num3) / 3))