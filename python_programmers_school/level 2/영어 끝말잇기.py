def solution(n, words):
    for i in range(1, len(words)):
        if (words[i][0] != words[i-1][-1]) or (words[i] in words[:i]):
            return [i%n+1, i//n+1]
    else:
        return [0, 0]

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


# 다른 풀이
def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    answer = [turn%n +1, turn//n + 1]
    if turn == 0:
        answer = [0, 0]
    return answer