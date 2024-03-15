def solution(n):
    result = []
    while divmod(n, 3):
        result.append(divmod(n,3)[1])
        n = divmod(n,3)[0]
        if n == 0: # 아예 몫이 0이 될 때까지 나눠야 한다.
            result.reverse()
            break
    answer = 0
    for i in range(len(result)):
        answer += result[i]*3**i
    return answer




# 이전에 틀린 코드

def solution(n):
    result = []
    while divmod(n, 3):
        result.append(divmod(n,3)[1])
        n = divmod(n,3)[0]
        if n == 1: # 변경
            result.append(1) # 제거
            result.reverse()
            break
    answer = 0
    for i in range(len(result)):
        answer += result[i]*3**i
    return answer

