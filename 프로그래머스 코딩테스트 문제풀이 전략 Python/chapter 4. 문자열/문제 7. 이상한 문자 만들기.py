def solution(s):
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0
        else:
            if cnt % 2 == 0:     # 각 단어별에서의 인덱스를 따지므로 cnt가 짝수인지 홀수인지를 따져야 한다. (i가 아니라)
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            cnt += 1
    return ''.join(s)

print(solution('You are  good'))