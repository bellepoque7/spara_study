def solution(n):
    answer = []
    for i in str(n):
        i = int(i)
        answer.append(i)
    answer.reverse()
    return answer
