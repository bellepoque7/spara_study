def solution(n):
    for i in range(1,n+1):
        if i ** 2 == n:
            i = i+1
            return i ** 2
        elif i == n:
            return -1
