str = input()

number = ""     # 숫자만 담기 위한 객체를 만들어 준다.
for i in str:     # i에 str의 한자한자가 대입된다.
  if i.isdigit():     # 문자 i가 str type의 숫자인지를 판단
    number += i     # 참일 경우 number에 i를 추가

for j in number:     # j는 number의 한자한자가 대입됨
  if j == "0":     # j가 "0"이면 그것을 없애주어야 함.
    number = number.replace(j, "", 1)     # replace를 사용할 때에는 항상 변수에 담아 주어야 한다. 그리고 replace는 문자열 안에서 해당하는 문자 모두를 치환하기 때문에 1개만 바꾸어 주고 싶으면 마지막에 개수를 적어 주어야 한다.
  else:     # 0이 아닌 숫자가 나오면 즉시 break    --> 앞쪽의 0만 제거될 수 있게 함
    break
print(number)     # 숫자 출력

number = int(number)      # 약수를 구하기 위해 str type의 number를 int type으로 형변환
count = 0     # 약수의 개수
for a in range(1, number+1):     # a는 number까지의 자연수
  if number % a == 0:     # number가 a로 나누어 떨어지면 그 a가 number의 약수가 됨.
    count += 1     # count 1 증가
print(count)     # count 출력