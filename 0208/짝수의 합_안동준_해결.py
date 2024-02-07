def solution(n):
    answer = 0
    for n in range(n+1):
        if n % 2 == 0:
            answer += n
    return answer
