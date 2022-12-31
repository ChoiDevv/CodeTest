# 로그인 성공?

def solution(id_pw, db):
    answer = "fail"
    id = id_pw[0]
    pw = id_pw[1]

    for i in range(len(db)):
        if id in db[i]:
            if pw == db[i][1]:
                answer = "login"
            else:
                answer = "wrong pw"
    
    return answer

print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))