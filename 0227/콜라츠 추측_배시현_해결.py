def solution(num):
    answer = 0
    while True:
        if num == 1:
            if answer >= 500:
                return -1
            else:
                return answer
        else:
            if num % 2 == 0:
                num = num / 2
                answer+=1
            else:
                num = num * 3 + 1
                answer+=1
