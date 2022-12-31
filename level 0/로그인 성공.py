def solution(id_pw, db):
        if id_pw in db:
            return "login"
        else:
            id_list = [db[i][0] for i in range(len(db))]
            if id_pw[0] not in id_list:
                return "fail"
            else:
                return "wrong pw"
              
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))

# 다른 풀이 1
# def solution(id_pw, db):
#     if db_pw := dict(db).get(id_pw[0]):     # --> dict 함수를 이용해 db list를 딕셔너리 type으로 변경, get 함수를 이용해 key(id)에 해당하는 value(pw) 부분만 뽑아내기!
#         return "login" if db_pw == id_pw[1] else "wrong pw"     # --> 만약 pw가 일치하면 login 출력, 그렇지 않으면 wrond pw출력(비번 확인 먼저 함)
#     return "fail"     

# 다른 풀이 2
# def solution(id_pw, db):
#     answer = 'fail'     --> 기본을 'fail'로 시작
#     for id, pw in db:     --> 이렇게 인덱싱 안해줘도 db에 있는 것을 id와 pw 변수에 각각 담을 수 있다.
#         if id_pw[0] == id:
#             if id_pw[1] == pw:
#                 answer = 'login'
#             else:
#                 answer = 'wrong pw'
#     return answer