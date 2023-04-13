def solution(s):
    prev = ''
    for i in range(len(s)):
        if (prev == ' ' or prev == '') and s[i].isdecimal() == False and s[i].islower():
            s = s.replace(s[i], s[i].upper(), 1)
        elif prev != ' ' and s[i].isupper():
            s = s.replace(s[i], s[i].lower(), 1)
        prev = s[i]
    return s

print(solution("for the last week"))