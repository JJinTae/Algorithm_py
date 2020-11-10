def solution(x):
    
    L = list(map(int, list(str(x))))
    
    return x % sum(L) == 0