# 개선된 코드
def solution(s):
    s = sorted(s[2:-2].split('},{'), key=len)
    answer = {}     # 주목! answer 변수를 배열이 아닌 객체(파이썬에서는 dictionary)로 변경한다.
    for tuples in s:
        elements = tuples.split(',')
        for element in elements:
            number = int(element)
            if number not in answer:    # 배열과 동일하게 in 문법을 사용하여 중복을 확인한다. 배열에서는 in을 쓰면 O(n)의 시간이 걸리지만, dic에서는 O(1)로 해결 가능하다.
                answer[number] = 1     # 중복 확인 시 딕셔너리의 키값만 보므로 값을 어떤 것으로 할당하더라도 문제가 없다.
    return list(answer)     # 결과를 다시 배열로 만든다. (딕셔너리를 배열로 만들면 딕셔너리의 키값만이 배열의 인자로 들어가기 때문에 바로 원하는 값을 얻을 수 있다.)

            


# 통과하지만 넣을 숫자가 중복으로 들어갔는지 검사하는 부분에서 개선이 필요한 풀이
def solution(s):
    # 1. 첫 중괄호를 제거하고 분리 기준을 잡는다.
    data = s[2: -2].split('},{')
    # 2. 튜플의 조건에 맞춰 쪼개진 문자열을 길이에 맞게 정렬한다.
    data = sorted(data, key=lambda x:len(x))
    answer = []
    # 3. 쪼갠 문자열을 한번 더 ',' 기준으로 쪼개진 숫자가 있는 문자를 찾는다.
    for item in data:     # item에는 튜플 한개가 들어감
        item = list(map(int, item.split(',')))     # , 기준으로 분리되어 나온 문자를 int형으로 바꿈 (애초에 , 기준으로 분리된 문자열은 숫자 문자열밖에 없으므로 오류 발생 X)
        for value in item:     # value는 , 기준으로 분리되어 나온 숫자만 들어감.
            if value not in answer:
                answer.append(value)
    return answer
            