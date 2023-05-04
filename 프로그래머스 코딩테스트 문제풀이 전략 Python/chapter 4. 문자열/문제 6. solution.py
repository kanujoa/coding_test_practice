def solution(s, n):
    # 1. 문자열을 배열로 만든다. (문자열 자체를 바로 수정하는 것은 불가하므로)
    s = list(s)
    # 2. 반복문으로 순회하면서 문자에 숫자를 더한다.
    for i in range(len(s)):
        if s[i] == ' ': continue
        corr = ord('A') if s[i].isupper() else ord('a')
        # (현재 글자의 숫자 - 알파벳 처음 위치 + 더해야 할 숫자) % 26 + 알파벳 처음 위치
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)
    # 3. 완성된 결과를 하나의 문자열로 만들어서 반환한다.
    return ''.join(s)