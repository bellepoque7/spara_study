def solution(s):
    answer = list(s)
    answer.sort()
    answer.reverse()
    return "".join(answer)
