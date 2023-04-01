# 역시 dic의 key값은 알파벳 하나하나여야 함.
# 같은 알파벳이 나오는 경우 기존 value값에서 1을 더함(누적)
# 새로운 알파벳일 경우 (key가 없는데)1을 누적하려고 하면 keyError가 난다. 
# 위와 같은 경우에 다음의 예시 적용(get 메서드 이용 : get은 인자로 들어온 key에 해당하는 value return) ex) dic[A] = dic.get('A', 0) + 1 (dic dictionary에 'A' key값이 없다면 0을 return 후 그 값에 1을 더한 값을 dic[A]에 할당함.)
# 위 방법을 사용하면 if문 in 이런 것들을 쓰지 않음과 동시에 같은 알파벳이 나왔을 경우도 해결 가능!

a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:     # 첫번째 문자열
    str1[x] = str1.get(x, 0) + 1      # 누적
for x in b:     # 두번째 문자열
    str2[x] = str2.get(x, 0) + 1     # 누적
for i in str1.keys():      # str1 dic의 key값들만 뽑아냄. (그것들이 i에 할당됨.)
    if i in str2.keys():     # i가 str2 dic의 key값 중 하나라면
        if str1[i] != str2[i]:     # 두 dic에서 그 key값의 value값이 서로 다르다면 알파벳 개수가 다른 것이기 때문에
            print("NO")     # NO 출력 후 끝내기
            break
    else:     # i가 str2 dic의 key값에 해당하지 않는 경우라면
        print("NO")     # 역시 NO 출력 후 끝내기
        break
else:
    print("YES")  