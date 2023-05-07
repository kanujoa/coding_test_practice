# 함정을 간파하고 코드를 작성하기
def solution(s):
    stack = []
    # 1. 받은 문자열을 for문으로 한 글자씩 읽는다.
    for case in s:
        # 2-1. 배열의 길이가 0이 아니고, 마지막 알파벳과 현재 순회 중인 알파벳이 같다면 배열에서 해당 요소를 제거한다.
        if stack and stack[-1] == case: stack.pop()
        # 2-2. 배열의 길이가 0이면 배열에 현재 순회 중인 알파벳을 넣는다. 
        else: stack.append(case)
    # 3. 모든 문자열을 다 돌았을 때 배열에 값이 없다면 모두 짝지은 것이고, 남아 있다면 모두 짝짓지 못한 것이다.
    return 0 if stack else 1      

# 함정을 확인하지 않은 채로 코드 작성하기
def solution(s):
    while len(s) > 1:     # 문자열이 남아 있는 동안
        s = list(s)      # 문자열을 문자 배열로 변환
        for i in range(len(s) - 1):     # 마지막 배열 인덱스는 항상 s의 길이 - 1보다 1이 작아야 한다.
            if s[i] == s[i + 1]: s[i] = s[i + 1] = ''     # 현재 문자와 다음 문자가 같으면 그 두 자리를 공백으로 변경

        new_s = ''.join(s)     # 문자열을 합치면서 공백 자동 제거
        if len(s) == len(new_s): break     # 변화가 없으면 제거하지 못했으므로 반복문 탈출
        s = new_s     # 변화가 있다면 s를 new_s로 업데이트

    return 1 if len(s) == 0 else 0     # 문자열 s의 길이가 0이면 1을 반환하고, 다 삭제되지 않아 길이가 1 이상이면 0을 반환한다.