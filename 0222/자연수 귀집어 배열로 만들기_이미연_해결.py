def solution(n):
    answer = []
    a = reversed(str(n))
    for i in a:
        answer.append(int(i))
    return answer
