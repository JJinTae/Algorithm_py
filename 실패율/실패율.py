def solution(N, stages):
    result = {}
    num = len(stages)
    for stage in range(1, N+1):
        if num != 0:
            failure = stages.count(stage)
            result[stage] = failure / num
            num -= failure
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
