def solution(n):
    result = []
    while divmod(n, 3):
        result.append(divmod(n,3)[1])
        n = divmod(n,3)[0]
        if n == 1:
            result.append(1)
            result.reverse()
            break
    answer = 0
    for i in range(len(result)):
        answer += result[i]*3**i
    return answer
