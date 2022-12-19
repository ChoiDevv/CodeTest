# 과제 안 내신 분..?

n = 30
student_list = list(range(1, 31))
attendance_list = []

for i in range(28):
    student = int(input())
    attendance_list.append(student)

answer = sorted(list(filter(lambda student: student not in attendance_list, student_list)))

print(answer[0])
print(answer[1])