# ascii 코드와 리스트를 이용한 풀이 (C++ 처럼 코드 짜기)
# A~Z: 65 ~ 90, a~z: 97~122

a = input()
b = input()
str1 = [0] * 52     # 알파벳 대문자 26개, 소문자 26개 
str2 = [0] * 52     # 마찬가지
for x in a:     # a 문자열에서
    if x.isupper():     # x가 대문자일 경우
        str1[ord(x)-65] += 1     # 대문자는 A부터 Z까지 차례로 인덱스가 0부터 25이어야 한다는 것을 고려해 인덱스 코드 작성하기
    else:     # x가 소문자일 경우
        str1[ord(x)-71] += 1     # 소문자는 a부터 z까지 차례로 인덱스가 26부터 51이어야 한다는 것을 고려해 인덱스 코드 작성하기
for x in b:     # b 문자열에서도 똑같이 적용하기 (str2에 똑같이 적용하기)
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1
for i in range(52):
    if str1[i] != str2[i]:     # str1의 요소와 str2의 요소에서 다른 부분이 있다면 
        print("NO")     # NO 출력하고 중단!
        break
else:     # 다른 부분이 없어 break 걸리지 않았다면
    print("YES")     # YES 출력!