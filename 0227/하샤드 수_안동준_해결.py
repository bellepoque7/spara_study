def solution(x):
    sum1 = sum(int(x_num) for x_num in str(x))
    if x % sum1 == 0:
        return True
    else:
        return False
