def solution(seoul):
    answer = -1
    for search in seoul:
        if search == "Kim":
            answer += 1
            break
        else:
            answer += 1
    return "김서방은 %s에 있다" % answer
