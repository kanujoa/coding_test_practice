import sys
input = sys.stdin.readline
n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
def modify(score):
    return score/m*100
print(sum(list(map(modify, scores))) / n)

# 간단한 풀이
# N=int(input())     --> 과목 수
# L=list(map(int,input().split()))     --> 시험 점수를 모두 리스트로 변환     
# print(sum(L)/max(L)*100/N)     --> 나누어서 더하나 더해서 한꺼번에 더하나 같음! 따라서 한번에 계산함.