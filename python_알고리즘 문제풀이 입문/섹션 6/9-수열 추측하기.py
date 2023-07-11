import copy

# 순열을 구하는 함수
def permutation(L):
    global ch, pick, res
    if L == n:     # 트리의 레벨이 가장 윗줄 숫자 개수인 n과 같아지면 
        res.append(list(num for num in pick))
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                pick.append(nums[i])
                permutation(L + 1)
                ch[i] = 0
                pick.pop()

# 가능한 순열을 모두 돌면서 문제에서 주어진 방식대로 합을 구해 (파스칼 삼각형) f와 일치하면 해당 순열의 숫자를 차례로 출력한다.
def get_answer(cpy, n, r):
    if n == 1 and cpy[0] == f:
        for num in r:
            print(num, end=' ')
        exit()
    elif n == 1:
        return
    else:
        for i in range(n-1):
            cpy[i] = cpy[i] + cpy[i + 1]
        cpy.pop()
        return get_answer(cpy, n - 1, r)

n, f = map(int, input().split())     # n : 가장 윗줄 숫자 개수, f : 가장 밑 줄에 있는 수
nums = [i + 1 for i in range(n)]     # 순열을 만들 수의 종류
ch = [0] * len(nums)     # 어떤 숫자가 뽑혔는지를 기록할 리스트 (중복으로 뽑히면 안되므로)
pick = []     # 어떤 숫자를 뽑았는지 기록할 리스트     
res = []     # 가능한 순열의 결과를 모두 담을 리스트
permutation(0)

for r in res:
    cpy = copy.deepcopy(r)
    get_answer(cpy, n, r)