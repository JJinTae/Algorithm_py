def solution(n):

    if n == 2:
        return 1
    
    result = set([*range(3, n+1, 2)])
    answer = 1
    next = 3
    while n**(1/2)+1 >= next:
        result -= set(range(next, n+1, next))
        answer += 1
        next = sorted(list(result))[0]
    return answer + len(result)

    
    """
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
    """        
    return 1
    """

    """
    for i in result:
        flag = False
        for j in result:
            print(i, " 비교 ", j)
            if i == j and i % j == 0:
                flag = True
                break
            if j > i:
                break

        if flag:
            for k in range(2, n, 1):
                if n < k*i:
                    break
                elif k*i % 2 != 0:
                    try:
                        print('remove', i*k)
                        result.remove(i * k)
                        # print('remove 수행 후 ', result)
                    except:
                        print('exception ')
                        pass

    return len(result) + 1
    """

    """
    for i in result:
        print(i)
        for j in result:
            if i % j == 0:
                for k in range(2, n, 1):
                    if n < k*i:
                        break
                    elif k*i % 2 != 0:
                        try:
                            # print('remove', i*k)
                            result.remove(i * k)
                            # print('remove 수행 후 ', result)
                        except:
                            # print('exception ')
                            pass
            break


    # print(result)
    return(len(result)+1)
    """


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
