def solution(n):
    answer = 0
    for i in range(1, n+1):
        for ii in range(1, n+1):
            if i * ii == n:
                answer+=i
    return answer
