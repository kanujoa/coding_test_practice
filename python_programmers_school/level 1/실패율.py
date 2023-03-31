# zeroDivisionError 에러 대비를 위해 if len(stages) == 0일 때의 처리 코드를 넣어주는 것이 중요하다.
# 실패율이 높은 순으로 정렬하되 실패율이 같은 경우 작은 번호의 스테이지가 먼저 오도록 정렬하는 것은
# sorted 함수에 key = lambda x: x[0] 조건과 reverse=True 조건을 함계 넣어줌으로써 구현 가능하다.

def solution(N, stages):
    fail_rates_stages = []
    for s in range(1, N+1):
        if len(stages) == 0:
            fail_rates_stages.append((0, s))
        else:
            fail_rate = stages.count(s) / len(stages)
            fail_rates_stages.append((fail_rate, s))
            stages = list(filter(lambda x: x != s, stages))
    
    fail_rates_stages = sorted(fail_rates_stages, key = lambda x: x[0], reverse=True)
    
    return [result[1] for result in fail_rates_stages]

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4, 4]))
print(solution(N = 5, stages = [3, 1, 2, 2, 2]))


# 다른 풀이 (이게 훨씬 더더더더더더 빠름.)
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)     # info는 각 stage에 머물러 있는 사람의 수를 나타내는 리스트, 처음에는 값을 모두 0으로 초기화
    for stage in stages:          
        info[stage] += 1      # 특정 stage가 나올 때마다 그 stage 숫자에 해당하는 인덱스의 값에 +1을 함.  
    for i in range(N):
        be = sum(info[(i + 1):])     # 스테이지에 도달한 사람의 수는 인덱스 i+1의 값부터 끝까지의 값을 더한 값임. (i는 0부터 시작하므로 1을 더해줌.)
        yet = info[i + 1]     # 아직 해당 스테이지를 클리어하지 못한 사람의 수는 인덱스 i+1에 해당하는 값임.
        if be == 0:     # be가 0이면 
            fail.append(i + 1, 0)     # fail 리스트에 (스테이지, 실패율(0)) 쌍 추가 (스테이지에 도달한 사람이 아무도 없으므로 실패율 또한 0임.)
        else:     # be가 0이 아닌 경우
            fail.append(i + 1, yet / be)     # fail 리스트에 (스테이지, 실패율(yet/be의 값)) 쌍 추가
    for item in sorted(fail, key=lambda x: x[1], reverse=True):     # fail 리스트를 실패율 기준으로 내림차순으로 정렬 (같은 실패율이 있을 경우 스테이지가 낮은 것 먼저 배치됨.)
        answer.append(item[0])     # 답 리스트인 answer 리스트에 스테이지 부분만 추가함.
    return answer