# 최초 오답
def solution(n):
    for i in range(1, n):
        if i % 2 == 0:
            sum += n
        else:
            pass
    return answer


# 아래와 같이 수정함 
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            answer = answer + i
    return answer
