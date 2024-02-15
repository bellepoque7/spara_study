def solution(n):
    x = 2  
    while n % x != 1:  # n을 x로 나눈 나머지가 1이 아닌 경우에 계속 반복
        x += 1  
    return x


