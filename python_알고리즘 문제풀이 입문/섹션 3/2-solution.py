s = input()     # 문자열 입력 받기
res = 0
for x in s:
  if x.isdecimal():     # isdecimal은 0부터 9까지의 숫자만 찾아주고, isdigit는 모든 숫자 형태를 다 찾아준다.(제곱같은 것이 들어와도 다 판별 가능)
    res = res * 10 + int(x)     # 이렇게 하면 앞부분에 나오는 0은 제외하고 바로 숫자를 만들 수 있음.
print(res)     # 숫자 출력

cnt = 0     # 약수 count
for i in range(1, res + 1):
  if res % i == 0:
    cnt += 1
print(cnt)