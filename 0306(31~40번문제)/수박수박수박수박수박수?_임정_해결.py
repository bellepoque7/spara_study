def solution(n):
    answer = ''
    my_str = '수박'
    answer =  my_str * (n//2)
    if n % 2 == 1:
        answer = answer + '수'
    return answer
