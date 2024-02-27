def solution(x):
    # 기능1) 자릿수의 합을 기능을 구현(ex 18 -> 1 + 8 -> 9 )
    # 변수 sum
    # 몫/나머지 기능 내장함수, 연산자(//, %)
    # 자릿수의 합을 구하기 위해서 무한대로 나눠야할 수도있으나
    # 10000이므로 최대 4번까지만 나누면 될듯 
    # 이방식은 while
    n = x # 처음 들어온 수를 따로 저장
    sum = 0

    while x >10:
        remain = x % 10  # 나머지: 한자리수 특징
        x = x // 10
        sum = sum + remain
        # print("나머지",remain,"몫", x, "합", sum) # 루프마다 진행되는 진척을 확인
    sum = sum + x #sum : 문제에서 요구하는 자릿수의 합
    
    # 기능2) x를 a로 나눠서 나누어 떨어지는지 체크
    if n % sum == 0: # 나누어 떨어진다면
        return True
    else:
        return False
    
    
    
    
