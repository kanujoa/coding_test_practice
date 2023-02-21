# 더 짧게 작성하기 (but 아래처럼 reverse해서 짜는 것보다 첫번째 방법대로 직접 짜는 것이 좋음. 면접에서는 직접 구현하는 것이 좋음.)
n = int(input())
for i in range(n):
  s = input()
  s = s.upper()
  if s == s[::-1]:     # s(문자열)을 뒤집은 것(s[::-1])이 원래 문자열 s와 같은지를 확인 --> 같으면 회문 문자열
    print("#%d YES" %(i + 1))
  else:
    print("#%d NO" %(i + 1))