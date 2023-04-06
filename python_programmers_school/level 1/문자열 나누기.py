# def solution(s):
#     result = 0
#     while True:
#         x_cnt = 1
#         other_cnt = 0
#         for i in range(1, len(s)):
#             if s[i] == s[0]:
#                 x_cnt += 1
#             else:
#                 other_cnt += 1
#                 if x_cnt == other_cnt:
#                     result += 1
#                     s = s[i+1:]
#                     if s == '':
#                         return result
#                     break
#         else:     # 이 코드가 없으면 아래의 3번째 케이스 같은 경우(x_cnt가 other_cnt보다 많아 x_cnt == other_cnt의 경우가 생기지 않는 경우)
#             return result + 1     # 에 무한 루프가 되어 시간 초과가 발생한다.
        # 그리고 3번째 테스트 같은 경우에는 split할 수 없는 경우가 되므로 그냥 한 뭉텅이로 들어간다. 따라서 +2가 아닌 +1을 해 주어야 한다.
                  
# print(solution("banana"))
# print(solution("abracadabra"))
# print(solution("bbbcc"))


# 더 명료한 풀이
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:     # i는 s의 문자 하나하나
        if sav1==sav2:     # sav1과 sav2가 같다면
            answer+=1     # answer에 1 추가 (맨 처음 1 추가는 모든 문자열의 분해 결과로 최소 1이 될 수 밖에 없으므로 일어나는 것으로 생각)
            a=i     # a(첫번째 문자)가 i(현재 문자)가 됨. 
        if i==a:     # i가 a와 같은 문자라면 (여기가 elif가 아닌 if인 점 주목!)
            sav1+=1     # 첫번째 문자와 같은 문자의 개수를 담는 변수에 해당하는 sav1에 1 추가
        else:     # i와 a가 다른 문자라면
            sav2+=1     # 다른 문자의 개수를 담는 변수에 해당하는 sav2에 1 추가
    return answer

print(solution("banana"))
