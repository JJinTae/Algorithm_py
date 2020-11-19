def solution(n, arr1, arr2):
    answer = []
    
    for i in range (n):
        tmp_line1 = decTobin(n, arr1[i])
        tmp_line2 = decTobin(n, arr2[i])
        tmp_str = ''
        for j in range(n):
            if tmp_line1[j] == '1' or tmp_line2[j] =='1':
                tmp_str += '#'
            else:
                tmp_str += ' '
        answer.append(tmp_str)
    
    return answer



# 10진수를 2진수 #으로 변환하는 함수
def decTobin(n, num):
    binary = ''
    while num > 0:
        binary = binary + str(num%2)
        num //= 2
    
    binary += '0'*(n - len(binary))
    return binary[::-1]