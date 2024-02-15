def solution(a, b):
    if a == b:
        return a
    elif a < b:
        answer = 0
        for num in range(a, b+1):
            answer += num
        return answer
    else:
        answer = 0
        for num in range(b, a+1):
            answer += num
        return answer
