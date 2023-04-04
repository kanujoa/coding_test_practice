# def solution(s):
#     result = [-1]
#     for i in range(1, len(s)):
#         for j in range(1, i+1):
#             if s[i] == s[i-j]:
#                 result.append(j)
#                 break
#         else:
#             result.append(-1)
#     return result



# 다른 풀이 (딕셔너리를 이용한 풀이, 훨씬 더 효율적!)
# dic는 중복되는 key를 가질 수 없다! 따라서 아래 dic[s[i]] = i 코드 실행 시 dic에 이미 s[i] 키가 존재한다면 그 키의 
# 값이 i로 업데이트 됨. 새로 추가되는 것이 아님!
def solution(s):
    answer = []
    dic = dict()     # --> 처음에는 빈 dic
    for i in range(len(s)):     # --> 문자열의 길이만큼의 인덱스  
        if s[i] not in dic:     # --> dic에 해당 알파벳이 없다면     
            answer.append(-1)     # --> answer에는 -1 추가
        else:     # --> dic에 해당 알파벳이 있다면
            answer.append(i - dic[s[i]])     # --> answer에 해당 알파벳의 인덱스와 똑같은 알파벳 인덱스 사이의 거리를 append
        dic[s[i]] = i     # --> 항상 dic에 알파벳과 그의 인덱스 추가

    return answer

print(solution("banana"))