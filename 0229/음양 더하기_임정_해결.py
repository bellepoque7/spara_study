def solution(absolutes, signs):
    answer = 0 
    
    for i in range(len(absolutes)): # 0 , 1, 2
        # 부호 체크
        if signs[i] == True:
            answer = answer + absolutes[i] # 양수면 그냥 더한다
        else: # 음수이면
            answer = answer - absolutes[i]       
    return answer
