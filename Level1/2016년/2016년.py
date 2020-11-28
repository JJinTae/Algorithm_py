def solution(a, b):
    
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    return weekdays[(sum(month[:a-1]) + b-1) % 7]
    
    # 2016-1-1은 금요일이다.
    # 테스트 케이스 5 24
    
    # 0 ~ 4 더해준다.
    # 1 + 31 + 29 + 31 + 30 = 
    
    # 2016-2-1은?
    # 2-1 1까지
    # 1+0+31 = 32
    # 32 % 7 = 4 - 1 한다.
    
    """
    for i in month[:a]:
        b += i
    """
