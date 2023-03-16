word = input()
lt = 0
rt = -1
for i in range(len(word)//2): 
    if word[lt+i] != word[rt-i]:
        print(0)
        break
else:
    print(1) 

# 간단한 방법
# alp =list(str(input()))      # --> 문자열을 받아 문자 하나하나를 요소로 만든 뒤

# if list(reversed(alp)) == alp:     # --> 그것을 뒤집어서 리스트 형태로 바꾼 결과가 alp와 같으면 (list()를 해주지 않으면 주소 형태로 나온다.)
#     print(1)     # 1 출력
# else:     
#     print(0)