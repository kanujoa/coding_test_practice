def solution(new_id):
    # 1. 문자열 전체를 소문자로 변환한다.
    answer = new_id.lower()

    # 2. 지정된 문자를 제외한 나머지 문자를 전부 제거한다.
    filtered = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):     # c가 알파벳인지 아닌지는 isalpha 메서드로 확인할 수 있다.
            filtered.append(c)
    answer = ''.join(filtered)

    # 3. 마침표가 2번 찍혔다면 그중 하나만 제거한다.
    # 아래와 같은 방식으로 한다면 굳이 리스트 사용 안해도 된다. 
    # 연속된 '.'이 짝수 개수로 존재하면 2개씩 사라져서 결국 '.'이 아예 사라지게 된다.
    # 연속된 '.'이 홀수 개수로 존재하면 2개씩 사라져서 결국 '.' 하나가 남게 된다.
    while '..' in answer:
        answer = answer.replace('..', '.')     # replace는 가장 먼저 발견된 것만 수정함!

    # 4. 마침표 양옆으로 문자열을 1개씩 제거한다.
    # strip 메서드를 사용하면 양 끝의 문자 제거가 가능하다.
    answer = answer.strip('.')

    # 5. 전부 제거했는데 아무것도 없으면 'a'를 할당한다.
    if answer == '': answer = 'a'

    # 6. 나온 결과가 16자 이상인 경우 그 이상은 모두 삭제, 마지막 문자가 따옴표인 경우 역시 삭제한다.
    if len(answer) > 15: answer = answer[:15]
    if answer[-1] == '.': answer = answer[-1]

    # 7. 반대로 3자 미만이라면 마지막 문자를 반복해서 3글자 이상으로 만든다.
    while len(answer) < 3:
        answer += answer[-1]     # 문자열 더하기 비용이 높지 않으므로 이정도는 가능!
    
    return answer