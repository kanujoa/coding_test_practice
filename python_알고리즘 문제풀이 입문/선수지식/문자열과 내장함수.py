'''
문자열과 내장함수
'''
msg = "It is Time"
print(msg.upper())     # 모든 문자 대문자화
print(msg.lower())     # 모든 문자 소자문
print(msg)     # 원본은 그대로 존재!
tmp = msg.upper()     # 대문자화 된 변수
print(tmp)
print(tmp.find("T"))     # 특정 문자를 찾아 인덱스 번호로 반환(가장 앞번호로)
print(tmp.count("T"))     # 특정 문자의 개수 반환
print(msg[:2])     # 문자열 슬라이싱
print(msg[3:5])

print(len(msg))     # 문자열 길이
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:     # 문자열에서는 range 사용 안하고 그냥 in으로 바로 사용 가능
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():     
        print(x, end=' ')     # 대문자만 출력(소문자 확인하기: islower())  
print()

for x in msg:
    if x.isalpha():     
        print(x, end='')     # 알파벳만 출력
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x))     # ord: 문자를 아스키 넘버로 (A: 65, Z: 90)

tmp = 'az'
for x in tmp:
    print(ord(x))     # (a: 97, z: 122)

tmp = 65
print(chr(tmp))     # chr: 아스키 넘버를 문자로

tmp = 66
print(chr(tmp))
