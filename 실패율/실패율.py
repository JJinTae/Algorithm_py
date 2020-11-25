from collections import Counter

def solution(N, stages):

    num = len(stages) # 사람 수를 저장
    failure = [0] * N # 실패율 저장
    stages = Counter(stages)

    for i in range(1, N+1):
        if stages[i] != 0:
            failure[i-1] = stages[i] / num
            num -= stages[i]

    answer = []
    num = len(failure)
    for i, item in enumerate(failure):
        m = item
        idx = i
        for j, _item in enumerate(failure[::-1]):
            if _item >= m :
                    m = _item
                    idx = num -1 -j
        answer.append(idx + 1)
        failure[idx] = -1

    return answer
