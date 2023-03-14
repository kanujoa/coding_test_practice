# def solution(s):
#     return int(s)     # int를 사용하면 "-1234"나 "+1234" 이렇게 되어있어도 자동으로 -1234, 1234 이런 식으로 변환된다.

# 자세하게 작성하기
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):     # 문자열 뒤집기
        if number == '-':     # -가 나타나면 
            result *= -1     # -1을 숫자에 곱해줌 (마지막 단계에 일어날 수밖에 없음.)
        else:
            result += int(number) * (10 ** idx)     # result는 1의 자리부터 채워짐.
    return result
print(strToInt("1234"))
# "1234"의 경우 "4321"로 뒤집히고, (0, 4), (1, 3), (2, 2), (3, 1) 이렇게 짝지어짐.
# 따라서 result = 1000 * 1 + 100 * 2 + 10 * 3 + 1 * 4 이렇게 됨.