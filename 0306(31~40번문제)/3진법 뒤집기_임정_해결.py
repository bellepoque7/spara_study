def solution(n):
    answer= ''
    #3진법을 계산하는법
    #3의 나누기의 나머지가 진법의 숫자가 되며, 순차대로 진행하면 앞뒤 반전
    
    while n > 0:
        #3으로 나눈 나머지를 문자열로 붙이기
        answer  += str(n%3)
        #몫을 업데이트
        n //= 3

    # int 함수는 전달인자를 통해 3진법 -> 10진법 표현이 가능    
    return int(answer,3)        
