def solution(babbling):
    able = {'aya': '1', 'ye': '2', 'woo': '3', 'ma': '4'}
    result = 0
    for i in babbling:
        prv = ''
        for j in able:
            i = i.replace(j, able[j])     # 말할 수 있는 단어는 숫자로 치환
        for x in i:
            if x.isdigit() == False or x == prv:     # x가 숫자인 문자가 아니거나 x가 바로 이전 단어와 같다면(연속된다면) 할 수 있는 단어가 아니므로
                break     # 반복문 빠져나가기
            prv = x
        else:     # break가 걸리지 않은 경우에는 
            result += 1     # 성공하였으므로 result에 1 더하기
    return result

# print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))


# 다른 풀이
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer