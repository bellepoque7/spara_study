def solution(x):
    m = x
    answer = 0
    while True:
        answer += x % 10
        if x // 10 == 0:
            break
        else:
            x = x // 10
    if m % answer == 0:
        return True
    else:
        return False
