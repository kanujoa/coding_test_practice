def solution(name, yearning, photo):
    result = []
    for i in photo:
        sum = 0
        for j in i:
            if j in name:
                sum += yearning[name.index(j)]
        result.append(sum)
    return result

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))