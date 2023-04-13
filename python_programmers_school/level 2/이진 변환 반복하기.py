def solution(s):
    result = [0, 0]
    while s != '1':
        while '0' in s:
            s = s.replace('0', '', 1)
            result[1] += 1
        s = str(bin(len(s)))[2:]
        result[0] += 1
    return result

print(solution("01110"))


# 간단한 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1     # while문의 실행문에 들어선 순간 이진 변환은 무조건 이루어지므로 a += 1을 적어줌.
        num = s.count('1')     # 어차피 '0'은 삭제해야 하기 때문에 이진 변환해야 할 숫자는 s에서의 '1'의 개수이다.
        b += len(s) - num     # 문자열은 '0' 또는 '1'로만 이루어져 있으므로 삭제해야 할 '0'의 개수는 s의 길이에서 '1'의 개수를 뺀 것이다.
        s = bin(num)[2:]     # num을 2진수로 변환한 것을 s로 업데이트한다. 변환하면 앞에 0b가 붙으므로 이를 없애기 위해 슬라이싱을 해줌.
    return [a, b]     # 리스트 형태로 반환