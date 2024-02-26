def solution(x):
    sum_x = sum(map(int,str(x)))
    if x % sum_x ==0:
        answer = True
    else:
        answer = False
    return answer   
