def solution(n, m):
    result = []
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    for i in range(1, m+1):
        if m % i == 0:
            answer.append(i)
    a = max(set(answer)&set(result))
    b = n*m / a
    return [a, b]
