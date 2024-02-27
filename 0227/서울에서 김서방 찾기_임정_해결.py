def solution(seoul):
    answer = ''
    # 인덱스를 하나씩 증가시키면서 해당하는 위치에 "Kim" 이라는
    #문자가 있는지 매번 확인하면 됨. 
    
    for i in range(len(seoul)): #리스트 길이만큼 루프돌려
        if seoul[i] == 'Kim':  # 해당 인덱스에 Kim이 있다면
            return f"김서방은 {i}에 있다"
