def solution(n):
    answer = 0
    for i in map(int, str(n)):
        answer += i
    return answer
