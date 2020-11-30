def solution(a, b):
    
    if a==b:
        return a
    elif a > b:
        a, b = b, a
        
    return sum(range(a, b+1))