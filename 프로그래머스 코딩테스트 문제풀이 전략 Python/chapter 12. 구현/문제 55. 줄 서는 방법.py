def w(n):
    if n == 0:
        return 1
    else:
        return n * w(n - 1)

def solution(n, k):
    people = [num for num in range(1, n+1)]     # 사람들의 번호를 오름차순으로 기록
    answer = []
    x = n     # n은 그대로 두고 n에 담긴 숫자는 활용하기 위해 x로 복사해 줌.
    while len(answer) != n:
        ways = w(x)     # 순열을 만드는 모든 경우의 수
        order = []     # 순열의 맨 앞 번호가 각각 몇 번째에서 처음 시작하는지 기록
        for i in range(len(people)):
            order.append([ways // x * i + 1, people[i]])     # 시작 번째수, 순열의 맨 앞번호
            if order[-1][0] > k:     # 우리가 원하는 번호(k번)보다 시작 번째수의 번호가 더 커질 때
                answer.append(order[-2][1])     # k번에 해당하는 순열에는 그 이전의 숫자가 먼저 들어가야 함.
                people.pop(people.index(order[-2][1]))     # 처리한 사람은 people 리스트에서 제거
                k = k - order[-2][0] + 1
                break
            elif order[-1][0] == k:     # k번과 시작 번째수의 번호가 같을 때
                answer.append(order[-1][1])     # k번에 해당하는 순열에는 그 숫자가 먼저 들어감.
                people.pop(people.index(order[-1][1]))     # 처리한 사람은 people 리스트에서 제거
                answer += people
                break
            elif len(order) == x and order[-1][0] < k:     # 첫번째 숫자가 order에 있는 수 중 가장 큰 수인 경우
                answer.append(order[-1][1])
                people.pop(people.index(order[-1][1]))
                k = k - order[-1][0] + 1
                break
        x -= 1     # 남은 숫자들 가지고 위 과정을 반복해야 하므로 x 1 감소
    return answer    
    
print(solution(3, 5))
# print(solution(3, 4))
# print(solution(4, 17))
# print(solution(5, 29))
# print(solution(3, 1))
# print(solution(3, 6))


# 다른 사람의 풀이
def setAlign(n, k):
    from math import factorial
    answer = []
    order = list(range(1,n+1))
    while n!=0 :
        fact = factorial(n-1)
        #answer.append(order.pop(k//fact-1 if k%fact ==0 else k//fact))
        answer.append(order.pop((k-1)//fact))
        n,k = n-1, k%fact     # 나머지 사용이 포인트!
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(setAlign(3, 5))