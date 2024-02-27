def solution(num):
    #주어진 수가 1인 경우에는 0
    if num == 1 :
        return 0

    i = 0 

    #짝수면 2로 나누고 
    #홀수면 3을 곱하고 1 을 더하기 

    while num != 1: # num 이 1이 되는 순간 while loop는 깨진다.
        # 500번 루프일때 함수 종료
        if i == 500:
            return -1
        i = i  + 1 #반복횟수 체크
        
        if num % 2 ==0: # 짝수라면
            num  = num // 2 
        else: #홀수라면
            num  = num *3  + 1
        # print(i, num) # 루프 진행할 떄마다 진척 상황 파악
        
    return i
