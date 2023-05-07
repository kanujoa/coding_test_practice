def solution(s):
    result = [0, 0]
    while s != '1':
        binary = ''
        origin_length = len(s)
        s = s.replace('0', '')     # 여기에서 replace를 사용하는 것보다 count 함수로 1의 개수를 세는 것이 더 효율적
        c = len(s)
        result[-1] += origin_length - c
        while c != 0:
            c, remainder = divmod(c, 2)
            binary += str(remainder)
        s = binary[::-1]
        result[0] += 1
    return result

print(solution("110010101001"))