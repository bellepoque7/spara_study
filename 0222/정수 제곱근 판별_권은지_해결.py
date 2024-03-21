
    
import math
def solution(n):
    sqrt_n =math.sqrt(n)
    if sqrt_n.is_integer():
        return int((sqrt_n +1) **2)
    else:
        return -1
