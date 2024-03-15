def solution(n):
    result = []
    while divmod(n, 3):
        result.append(divmod(n,3)[1])
        n = divmod(n,3)[0]
        if n == 0: # 삼진법을 아예 몫이 0이 될 때까지 해야했다.
            # result.append(1) 몫이 1이면 1을 넣는다는 한 자릿수일 때 해당되지 않음.
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
        if n == 1:
            result.append(1) # 몫이 1이 될때까지 나눈다 라는 생각이 맞지 않았음. ex) 1,2 등 몫이 0일 때가 무한루프.
            result.reverse()
            break
    answer = 0
    for i in range(len(result)):
        answer += result[i]*3**i
    return answer

