def solution(n):
    answer = 0
    for result in range(1,n+1):
        if result % 2 == 0:
            answer = answer + result
    return answer
