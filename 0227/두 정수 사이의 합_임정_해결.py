def solution(a, b):
    # a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수: range
    answer = 0
    
    #a가 더 크다면 일반적인 range함수로는 적용 안됨
    #min-max 함수를 쓰는게 더 깔끔
    if a > b:
        c = b
        d = a
    else:
        c = a
        d = b
    
    for i in range(c,d+1): # a~ b-1
        answer = answer + i
    return answer
