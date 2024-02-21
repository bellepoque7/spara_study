def solution(x, n):
    answer = []
    for o in range(1, n+1):
        answer.append(x*o)
    return answer
