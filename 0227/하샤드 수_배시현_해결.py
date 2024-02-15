def solution(x):
    m = x
    answer = 0
    while True:
        answer += x % 10 # 여기까지 더하고
        if x // 10 == 0:
            break # 반복문을 끝내라
        else:
            x = x // 10
    if m % answer == 0:
        return True
    else:
        return False
