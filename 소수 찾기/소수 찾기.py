def solution(n):
    if n != 2:
        count = 1
        result = [*range(3, n+1, 2)]
        
        
        
        for i in result:
            flag = True
            for j in range(3, i//2, 2):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                for k in range(2, n//i, 1):
                    try:
                        result.remove(i * k)
                    except Exception:
                        pass
        
        print(result)
        return(len(result)+1)
        
        
        
        """
        for i in range(3, n+1, 2): # 3 5 7 (9) 11 13 (15) 17 19 23 
            flag = True
            for j in range(3, i//2, 2):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                count += 1
        return count
        """
            
    return 1
