def solution(n, lost, reserve):
    
    
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
    
    
    
    
    """
    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve) - set(lost))
    
    for i in range(len(_lost)):
        for j in range(len(_reserve)):
            if _lost[i] == _reserve[j]-1 or _lost[i] == _reserve[j]+1:
                _lost[i] = -1
                _reserve[j] = -1
                break
    
    return n - (len(_lost) - _lost.count(-1))
    """