from itertools import combinations

def checkSlopeDifferent(line_1, line_2):
    a, b, e = line_1
    c, d, f = line_2
    if a * d - b * c == 0:
        return False
    return True

def getIntVertex(line_1, line_2):
    a, b, e = line_1
    c, d, f = line_2
    x = (b*f - e*d) / (a*d - b*c)
    y = (e*c -a*f) / (a*d - b*c)
    if x.is_integer() and y.is_integer():
        return (int(x), int(y))

def solution(line):
    answer = []
    vertex = set()
    for line_1, line_2 in combinations(line, 2):
        if checkSlopeDifferent(line_1, line_2):
            if getIntVertex(line_1, line_2) != None:
                vertex.add(getIntVertex(line_1, line_2))
    sort_x = sorted(list(vertex))
    min_x = sort_x[0][0]
    max_x = sort_x[-1][0]
    sort_y = sorted(list(vertex), key = lambda x: x[1])
    max_y = sort_y[-1][1]
    min_y = sort_y[0][1]
    for i in range(max_y, min_y-1, -1):
        dot = ['.'] * (max_x - min_x + 1)
        while True:
            if len(sort_y) != 0:
                if sort_y[-1][1] == i:
                    dot[sort_y[-1][0] - min_x] = '*'
                    sort_y.pop()
                else:
                    break
            else:
                break
        answer.append(''.join(dot))
    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))