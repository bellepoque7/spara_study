def solution(left, right):
    result = []
    answer = 0
    for i in range(left, right+1): # 14번 응용
        for x in range(1, i+1):
            if i % x == 0:
                result.append(x)
        if len(result) % 2 == 0:
            answer+=i
            result = []
        else:
            answer-=i
            result = []
    return answer
