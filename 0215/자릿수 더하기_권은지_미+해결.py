#def solution(N):
#    digit_sum = 0
#    while N > 0:
#        digit_sum += N % 10
#        N = N // 10  
#    return digit_sum

def solution(N):
    # 자릿수의 합을 저장할 변수를 초기화
    digit_sum = 0
    
    # N을 문자열로 변환하여 각 자릿수를 반복
    for digit in str(N):
        # 각 자릿수를 정수로 변환하여 sum
        digit_sum += int(digit)
    
    return digit_sum

