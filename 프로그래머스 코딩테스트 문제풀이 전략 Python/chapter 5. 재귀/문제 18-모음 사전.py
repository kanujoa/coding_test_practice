# 중복순열을 이용하여 모든 경우의 수 다 따져보기 (통과)'import itertools
import itertools

def solution(word):
    all_case = list(itertools.product(['', 'A', 'E', 'I', 'O', 'U'], repeat=5))
    for i in range(len(all_case)):
        all_case[i] = ''.join(list(all_case[i]))
    return sorted(set(all_case)).index(word)

# 테스트 케이스 2개만 통과...
def solution(word):
    cnt = 1 
    num = {'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    for letter in word:
        word = word.replace(letter, num[letter])
    word += '0' * (5 - len(word))
    while word != '10000':
        # 1. 뒤의 4자리가 모두 0000인 경우 (알파벳 하나인 경우)
        if word[1:] == '0000':
            word = str(int(word) - 1555)
        # 2. 끝이 0인데 0 제외 모든 구성 숫자가 같은 경우
        elif len(set(word)) == 2 and '0' in set(word):
            word = word[:word.index('0')-1] + '0' * (5 - word.index('0') + 1)
        # 3. 끝이 0이 아닌데 모든 구성 숫자가 같은 경우
        elif len(set(word)) == 1:
            word = word[:-1] + '0'
        # 4. 끝이 0인 경우 (위에 경우에서 걸러져서)
        elif word[-1] == '0':
            word = str(int(word) - 5)
        # 5. 끝이 0이 아닌 경우 (위의 경우에서 걸러져서)
        elif word[-1] != '0':
            word = str(int(word) - 1)
        cnt += 1
    return cnt

# print(solution("AAAAE"))
print(solution("AAAE"))

# RecursionError...

def search(word, cnt):
    if word == '10000':
        return cnt
    elif word[1:] == '0000':
        search(str(int(word) - 1555), cnt + 1)
    elif len(set(word)) == 2 and '0' in set(word):
        word[word.index('0') - 1] == '0'
        search(word, cnt + 1)
    elif len(set(word)) == 1:
        word = word[:-1] + '0'
        search(word, cnt + 1)
    elif word[-1] == '0':
        search(str(int(word) - 5), cnt + 1)
    elif word[-1] != '0':
        search(str(int(word) - 1), cnt + 1)

def solution(word):
    num = {'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    for letter in word:
        word = word.replace(letter, num[letter])
    search(word, 0)

print(solution("AAAAE"))