from collections import Counter
import numpy as np

def solution(N, stages):
    
    # 스테이지별 도전횟수 index는 스테이지 = index + 1
    challenges = [0] * (N + 1) # 도전횟수
    clear = [0] * (N + 1) # 클리어횟수
    failure = [0] * N # 실패율
    
    # 현재 도전중인 stages -> 이전의 stages는 클리어했다.
    # 실패율 구하는 알고리즘
    for key, value in Counter(stages).items():
        for i in range(key):
            challenges[i] += value
        for i in range(key-1):
            clear[i] += value
        
    for i in range(len(clear)):
        if clear[i] != 0:
            failure[i] = ((challenges[i] - clear[i]) / challenges[i]) + 1
    
    
    
    
    print(Counter(stages))

    print('clear : ', clear)
    print('challenges', challenges)
    print('failure', failure)
    
    
    
    answer1 = (-np.array(failure)).argsort()[:N]+1
    print(answer1)
    return answer1.tolist()
