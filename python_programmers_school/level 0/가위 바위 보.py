def solution(rsp):
    result = []
    for i in rsp:
        if i == "2":
            result.append("0")
        elif i == "0":
            result.append("5")
        elif i == "5":
            result.append("2")
    return "".join(result)

# 다른 풀이 1(딕셔너리 이용)
# def solution(rsp):
#     d = {'0':'5','2':'0','5':'2'}     --> value는 key를 이기는 값으로 설정  
#     return ''.join(d[i] for i in rsp)

# 다른 풀이 2(문자열만 이용, 속도 빠름)
# def solution(rsp):
#     rsp =rsp.replace('2','s')
#     rsp =rsp.replace('5','p')
#     rsp =rsp.replace('0','r')     --> 여기까지 먼저 숫자로 된 것을 rsp의 알파벳으로 바꿈.(rock, sissor, paper)
#     rsp =rsp.replace('r','5')
#     rsp =rsp.replace('s','0')
#     rsp =rsp.replace('p','2')     --> 여기까지 rsp 각각을 이길 수 있는 숫자로 replace함.
#     return rsp     --> 최종 결과는 숫자로 된 문자열이 나옴.