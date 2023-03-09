# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#   r, s = input().split()
#   res = ""
#   for i in s:
#       res += i * int(r)
#   print(res)

# 살짝 더 간단한 풀이
t=int(input())
for _ in range(t):
    n,s=input().split()
    for i in s:
      print(i*int(n),end="")     # --> 여기서 바로 i*int(n)을 하여 end=""으로 옆으로 공백 없이 나란히 출력되게 하면 코드가 더 간단해진다.
    print()     # print()을 작성해 주는 이유는 줄바꿈을 위해서이다. --> 문자열 두번째 이상의 입력시 줄바꿈이 되지 않은 상태로 입력된다.