word = input()     # 단어 입력 받기

# 대소문자를 구분하지 않고, 출력 결과는 대문자 또는 ?이므로 단어를 대문자로 바꾸어 줌.
word = word.upper()

alphabet_cnt = {}     # 각 단어의 개수를 세서 기록할 딕셔너리
for alphabet in word:     # word의 한 글자씩 탐색
    if alphabet not in alphabet_cnt:     # 딕셔너리에 alphabet이 key로 존재하지 않을 경우
        alphabet_cnt[alphabet] = 1     # value를 1로 하여 추가
    else:     # 딕셔너리에 alphabet이 key로 존재할 경우
        alphabet_cnt[alphabet] += 1     # 해당 value에 1 더하기

cnt = list(alphabet_cnt.values())     # 각 글자의 개수만 모은 리스트
if cnt.count(max(cnt)) > 1:     # cnt의 최대값이 여러개 존재할 경우 (최대값이 중복될 경우)
    print('?')     # 물음표 출력
else:      # cnt에서 최대값이 1개일 경우
    idx = cnt.index(max(cnt))     # idx는 cnt에서 최댓값의 인덱스 번호
    items = list(alphabet_cnt.items())     # alphabet의 key값과 value값을 짝지은 것을 요소로 하는 items 생성
    print(items[idx][0])     # 해당 문자 출력


# 다르게도 풀어보기
import sys
input = sys.stdin.readline

word = input().upper()     # 단어를 입력받은 후 각 알파벳을 모두 대문자로 만들기

alphabets = set(word)     # word에서 여러 번 등장하는 알파벳의 중복을 없애어 word가 어떤 종류의 알파벳으로 구성되어 있는지를 알아내기

cnt = 0     # 가장 많이 등장한 횟수 (초깃값 0)
_max = []     # 가장 많이 등장한 알파벳 기록

for alphabet in alphabets:     # 등장하는 알파벳 하나하나씩 탐색
    if word.count(alphabet) > cnt:     # word에서 현재 알파벳이 이전까지 가장 많이 등장한 횟수보다 더 많이 등장하였다면 
        cnt = word.count(alphabet)      # cnt를 현재 알파벳 등장 횟수로 초기화
        _max = [alphabet]     # 가장 많이 등장한 알파벳을 현재 알파벳으로 리셋
    elif word.count(alphabet) == cnt:     # 현재 알파벳 등장 횟수가 이전까지 최대 등장 횟수와 같다면 
        _max.append(alphabet)      # 리셋하지 않고 그 알파벳을 가장 많이 등장한 알파벳 리스트에 추가
if len(_max) > 1:     # _max 리스트의 길이가 1보다 크면 최대 등장 횟수가 같은 알파벳이 여러개라는 의미이므로
    print('?')     # ? 출력
else:     # _max 리스트의 길이가 1이면 가장 많이 등장한 알파벳이 하나이므로
    print(_max[0])     # 그 알파벳 출력 (_max 리스트의 0번 요소이다.)