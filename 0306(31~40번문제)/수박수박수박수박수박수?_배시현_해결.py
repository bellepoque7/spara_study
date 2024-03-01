def solution(n):
    answer = []
    for result in range(1, n+1):
        if result % 2 == 1:
            answer.append("수")
        else:
            answer.append("박")
    return ''.join(answer)
