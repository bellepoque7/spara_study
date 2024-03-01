def solution(a, b):
    answer = list(zip(a, b))
    result = []
    for i in answer:
        result.append(i[0]*i[1])
    return sum(result)
