submit = set([int(input()) for _ in range(28)])     # 제출한 학생 번호 (총 28명, 입력이 들어감)
students = set([i for i in range(1, 31)])      # 전체 학생 번호 (총 30명, 1번부터 30번까지)
result = list(students - submit)     # 차집합 이용(위에서 set으로 집합 형태로 바꿔줌), 후에 한줄씩 하나의 값을 출력하기 위해 list로 변환
result.sort()     # 리스트 오름차순 정렬
for r in result:
    print(r)     # 값 출력

# 더 효율적인 풀이
# x=list(map(int,range(1,31)))     --> 전체 학생
# for i in range(28):     
#     x.remove(int(input()))     --> 입력값을 한줄에 하나씩 받아 그 값을 위 x리스트에서 제거함.(28번 반복)
# for j in x:
#     print(j)     # 값 출력