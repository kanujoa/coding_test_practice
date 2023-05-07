def solution(s):
    # 1. 압축 가능한 길이만큼(전체 문자열 길이의 1/2 만큼) 순회한다.
    # 최종 압축 후 길이가 더 짧은지, 원래 문자열이 더 짧은지를 확인해야 하므로 answer 변수의 초깃값은 s의 길이이다.
    answer = len(s)
    for x in range(1, len(s) // 2 + 1):
        # 2. 반복된 규칙을 확인하여 몇 번 반복되었는지/반복된 문자열이 무엇인지 기록한 후 반영한다.
        comp_len = 0     # 압축된 문자열의 길이
        comp = ''     # 중복을 확인하기 위해 같은지 같지 않은지를 비교하기 위한 변수
        cnt = 1     # 문자가 반복된 횟수
        for i in range(0, len(s) + 1, x):     # i는 문자열을 나누는 기준이 되는 index (x가 step이다.)
            temp = s[i : i + x]     # 문자열 s에서 index i부터 i+x-1까지 자른다.
            if comp == temp:     # 만약 comp와 temp가 같다면 중복되는 문자열들이므로
                cnt += 1     # 그 개수를 세기 위해 cnt를 1 증가시킨다.
            elif comp != temp:     # comp와 temp가 다르면 서로 다른 문자열이므로
                comp_len += len(temp)     # comp_len에 현재 순회에 해당하는 문자열인 temp를 더한다.
                if cnt > 1:     # 여기에서 cnt가 1보다 큰 상태라면 앞에서 중복된 문자열이 있었다는 소리이므로 
                    comp_len += len(str(cnt))     # comp_len에 cnt를 str로 변환한 것의 길이를 더한다. (숫자가 항상 일의 자리 숫자가 아닐 수도 있으므로 += 1을 하면 안된다.)
                    cnt = 1     # cnt는 다시 1로 초기화
                comp = temp     # comp는 temp로 변경 (앞에서 나온 중복 문자열을 처리했으므로 이제 비교해야 할 대상이 temp이다.)
        # 3. 압축 과정에서 나온 문자열의 길이와 원래 문자열의 길이를 비교한다.
        answer = min(answer, comp_len)

    return answer

                
