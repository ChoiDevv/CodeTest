# 등수 매기기

def solution(score):
    average_list = []
    answer = []
    idx = 1

    for i in range(len(score)):
        average_list.append(sum(score[i]) / len(score[i]))
    
    average_sorted_list = sorted(average_list, reverse = True)

    for i in average_list:
        answer.append(average_sorted_list.index(i) + 1)
    
    return answer

print(solution([[1, 2], [1, 1], [1, 1]]))