def solution(n):
    answer = 0
    list_n = list(str(n))
    
    for i in list_n:
        answer+=int(i)

    return answer
