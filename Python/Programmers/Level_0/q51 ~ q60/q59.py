# 가위 바위 보

def solution(rsp):
    answer = ""

    for instance in rsp:
        if instance == "2":
            answer += "0"
        elif instance == "0":
            answer += "5"
        else:
            answer += "2"

    return answer