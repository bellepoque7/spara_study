def solution(numbers):
    
    # 문제를 풀거나 로직을 구현할때 
    # 1. 내장함수 쓰기(print, range)
    # 2. 다른 모듈에서의 함수를 쓴다(pandas)
    # 3. 직접 구현하기(사용자 함수 or 로직구현)
    
    num_sum = sum(numbers)
    num_len = len(numbers)
    
    return num_sum/num_len

    my_sum = 0 
    for i in numbers:
        my_sum = my_sum + i
    my_sum
