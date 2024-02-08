def solution(n):
    # 2, 4 -> 6 나와야 정답
    #input: 5 , output: 6
    answer = 0
    for i in range(1, n+1):
        #만약 i 가 짝수이면
        if i % 2 == 0:
            #print(i)
            # 기존 my_sum 에 해당 숫자를 더하여 다시 할당하라
            answer = answer + i  
    return answer

##요구사항 & 로직
# 전달인자 1개만 선언하면되는구나
# 짝수를 판별해야하는구나(조건)
# 더한다
# 옵션1) sum() 내장함수를 통해서 더한다 
# 옵션2) my_sum = 0  <- 계속 반복문을 통해서 더할 수도있음

##변수선언
# n
# my_sum 정수형자료형  = 0
