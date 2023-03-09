print(len(input().split()))          # input().split() 자체가 리스트로 출력해 준다.(문자를 입력하든 숫자를 입력하든)

# strip을 이용한 다른 풀이
# sentence = input()
# print(sentence.strip(' ').count(' ') + 1 if sentence != ' ' else 0)
# --> 입력으로 들어온 문자열을 sentence 변수에 넣고, 앞뒤 공백(' ')이 올 경우 제거하고(strip) 문장 안의 공백의 개수를 셈.(count 메서드) 
# 공백의 개수는 항상 단어 수보다 1 작으므로 1을 더한 값을 출력
