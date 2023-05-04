def solution(s):
    tuple_list = [[] for _ in range(s.count('}') - 1)]
    result = []
    idx = 0
    tmp = ''
    for i in list(s):
        if i == '}' and idx < len(tuple_list):
            tuple_list[idx].append(int(tmp))
            tmp =''
            idx += 1
        elif i.isdigit():
            tmp += i
        elif i == ',' and tmp != '':
            tuple_list[idx].append(int(tmp))
            tmp = ''
    tuple_list.sort(key=lambda x: len(x))
    for tuple in tuple_list:
        for num in tuple:
            if num not in result:
                result.append(num)
    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))