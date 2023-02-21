N = int(input())

for i in range(1, N+1):     # i는 case 번호에 해당한다.
  str = input().upper()     # 문자열 하나를 입력받는다. 대소문자 구별 안하므로 그냥 한번에 다 대문자로 만들어 버림.
  length = len(str)     # 문자열의 길이를 length 변수에 저장. 여기서 함수명인 len을 변수 이름으로 사용하게 되면 오류가 난다! (typerror: int object is not callable)
  for j in range(length // 2):     # j는 인덱스로 들어갈 것. 문자열의 양끝부터 가운데로 향하는 방식으로 확인할 것이기 때문에 length // 2 로 작성
    if str[j] != str[-1-j]:     # 양쪽의 문자가 같지 않으면 
      print(f"#{i} NO")     # #case 번호 NO를 출력하고
      break     # 바로 위의 for문을 빠져나감. 새로운 문자열 입력 후 위 for문이 다시 돌게 된다.
  else:     # for문이 break 없이 빠져나오면 회문 문자열이다.
    print(f"#{i} YES")     # 따라서 #case 번호 YES를 출력
    