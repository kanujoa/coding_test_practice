def solution(s):
    step = 1
    _min = 1001
    # 압축은 자신과 동일한 단어가 문자열 내에 존재할 때 가능하다.
    # 따라서 단어가 일정 길이 이상을 넘어가면 더 이상 동일한 단어를 찾을 수 없기 때문에 압축 가능한 최대 단어의 길이는 원래 주어진 단어의 1/2이다. 
    # 아래의 for _ in range(len(s))를 for _ in range(len(s) // 2 + 1)로 바꾸어 실행하면 불필요한 연산을 하지 않아 시간 단축이 가능하다.
    for _ in range(len(s)):  
        # 압축된 문자열(compression)을 구하여 길이를 구하는 것보다 변수를 하나 두어 바로바로 압축된
        # 문자열의 길이를 더하도록 만드는 것이 더 효율적이다.   
        compression = ''
        splits = []
        cnt = 1
        for i in range(0, len(s), step):
            if i + step <= len(s):
                splits.append(s[i: i+step])
            else:
                splits.append(s[i:])
        for i in range(len(splits) - 1):
            if splits[i] == splits[i + 1]:
                cnt += 1
            else:
                if cnt != 1:
                    compression += (str(cnt) + splits[i])
                else:
                    compression += splits[i]
                cnt = 1
        if cnt == 1:
            compression += splits[-1]
        else:
            compression += (str(cnt) + splits[-1])
        if len(compression) < _min:
            _min = len(compression)
        step += 1
    return _min

print(solution("abcabcdede"))