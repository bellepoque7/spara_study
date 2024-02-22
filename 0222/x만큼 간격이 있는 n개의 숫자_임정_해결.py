def solution(x, n):
    answer = []
    
    #x가 0 이라면
    if x == 0:
        return [0]*n     
    
    # x부터 시작해서, x 값마다 증가하고, x*n 까지 반복해서 숫자를 만들어라
    for i in range(x,x*(n+1),x):
        # print(i)
        answer.append(i)
    
    return answer
