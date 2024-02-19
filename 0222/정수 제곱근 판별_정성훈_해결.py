import math

def solution(n):
    answer = 0
    if math.sqrt(n).is_integer():
        answer = (math.sqrt(n)+1)**2
    else:
        answer = -1
    return answer
