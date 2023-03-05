import sys
play = True     # 굳이 play 변수에 bool 자료형을 넣어주지 않아도 된다. 그냥 break만 써도 됨.

# 예외처리와 반복문을 이용하여 해결!
while play:
  try:     # 예외 상황이 아닐 때는 2개의 수를 받아 더하기 연산 실행
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
  except ValueError:     # 값이 제대로 입력되지 않았을 때(ex) 값을 아예 입력하지 않았을 때) 프로그램 종료를 위해 ValueError 예외처리
    play = False     # ValueError 시 반복문 빠져나가기
# ValueError를 적어주지 않고 except만 적어주어도 된다.
       

# 더 효율적인 풀이
# import sys

# for x in sys.stdin:      --> sys.stdin은 줄 바꿈 문자를 포함한 입력을 목록으로 읽어들인다.
#     a, b = map(int, x.split())
#     print(a+b)