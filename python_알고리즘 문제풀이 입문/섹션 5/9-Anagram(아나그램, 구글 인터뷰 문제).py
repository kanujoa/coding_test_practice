first = input()
first_dic = dict()
second = input()
for s in first:     # solution에서 보면 이 for문의 실행문을 first_dic[s] = first_dic.get(s, 0) + 1 이렇게 한줄로 줄일 수 있다.
    if s in first_dic.keys():   
        first_dic[s] += 1
    else:
        first_dic[s] = 1
for s in second:
    first_dic[s] -= 1
for i in first_dic.values():
    if i != 0:
        print("NO")
        break
else:
    print("YES")