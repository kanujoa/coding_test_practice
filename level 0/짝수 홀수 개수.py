def solution(num_list):
    even = []
    odd = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    answer = [len(even), len(odd)]
    return answer


# 다른 사람의 풀이 1 
# def solution(num_list):
#     answer = [0,0]
#     for n in num_list:
#         answer[n%2]+=1     --> 이 코드의 인덱싱 부분 주목! 계산 결과 홀수는 자동으로 [0]이 되어 answer 리스트의 첫번째 부분, 짝수는 [1]이 되어
#                                리스트의 두번째 부분이 됨. 그리고 1은 계산시마다 무조건 한번씩 더해지게 되므로 횟수 증가 반영 가능
#     return answer


# 다른 사람의 풀이 2
# def solution(num_list):
#     div_num_list = list(map(lambda v: v % 2, num_list))     --> num_list의 요소 하나하나가 v에 대입, 2로 나눈 나머지가 리스트에 담기게 됨.
#                                                                 무조건 결과는 0(짝수) 아니면 1(홀수)
#     return [div_num_list.count(0), div_num_list.count(1)]     --> 0의 개수(짝수의 개수)를 첫번째 요소로, 1의 개수(홀수의 개수)를 두번째 요소로
#                                                                   하는 리스트를 반환함.
