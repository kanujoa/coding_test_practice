# 아스키 코드 --> 65~90 : A~Z, 97~122 : a~z
def solution(s, n):
    result = ""
    for i in s:
        if i != " ":
            a = ord(i)
            if a + n > 122:
                result += chr(96 + (a+n-122))
            elif 65<= a <= 90 and a + n > 90:
                result += chr(64 + (a+n-90))
            else:
                result += chr(a + n)
        else:
            result += " "
    return result 

# print(solution("AB", 1))
# print(solution("z", 1))
print(solution("a B z", 4))

# 다른 풀이
def caesar(s, n):
    s = list(s)     # 문자열을 리스트 형태로 바꾼다.
    for i in range(len(s)):     # i는 리스트 s의 인덱스
        if s[i].isupper():     # s[i]가 대문자면
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))     # 90 - 65 + 1 = 26
        elif s[i].islower():     # s[i]가 소문자면
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
        # s[i]가 공백인 경우는 그냥 넘어가게 된다.
    return "".join(s)