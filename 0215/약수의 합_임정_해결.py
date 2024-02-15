def solution(n):
    my_sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            my_sum = my_sum + i
    return my_sum
