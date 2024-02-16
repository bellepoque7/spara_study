def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort() # 헷갈
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return answer
