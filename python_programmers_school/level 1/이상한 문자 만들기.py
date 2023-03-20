def solution(s):
    cut = [a for a in s]     # s 문자열의 공백까지 한자한자 cut 리스트에 담는다. (공백은 한 자 이상이므로 단어 사이의 공백이 몇개가 될 지 모른다!)
    cnt = 0     # 공백이 나오면 0으로 초기화될 변수
    for i in range(len(cut)):     # 실제 인덱스 i
        if cut[i] == " ":     # 만약 현재 글자가 공백이면 
            cnt = 0     # cnt 0으로 초기화 (문제에서 단어당 인덱스 0으로 시작한다고 했으므로)
        else:     # 현재 글자가 공백이 아니라면
            if cnt % 2 == 0:     # 현재 cnt(단어당 인덱스)가 짝수라면
                cut[i] = cut[i].upper()     # cut 리스트에서 인덱스 i(실제 인덱스) 부분 요소를 대문자로 바꿈.
            else:     # 현재 cnt가 홀수라면
                cut[i] = cut[i].lower()     # cut 리스트에서 인덱스 i 부분 요소를 소문자로 바꿈.
            cnt += 1     # 대문자나 소문자를 바꾸는 과정을 거쳤으면 cnt 항상 1 증가
    return "".join(cut)     # 출력은 공백 없이 join하여 출력하면 원래 공백 개수가 어떻게 되든 그에 맞춰 올바르게 한 문장으로 출력됨.

print(solution("try hello world"))