def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
        answer.sort()
        answer.reverse()
    return int("".join(answer))
