def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    for i in arr:
        if len(answer) == 0 or i != answer[-1]:
            answer.append(i)


    """
    for i in range(len(arr)- 1) :
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
            
    answer.append(arr[-1])
    """
    return answer
