# 내 정답 풀이
def solution(n):
    answer = 0
    list_n = list(str(n))
    
    for i in list_n:
        answer+=int(i)

    return answer

# 튜터님 정답 풀이
def solution(n):
    answer = 0
    
    while True:
        answer = answer + n%10
        n = n//10
        
#        한자리 수 일 경우 계산
        if n // 10 == 0:
            answer = answer + n
            break
      
    return answer
