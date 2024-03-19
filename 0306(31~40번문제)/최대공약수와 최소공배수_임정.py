def solution(n, m):
    answer = []
    # 작은 값 정의
    min_num = min(n,m)
    # 최대 공약수 변수 정의, 기본 최대 공약수는 1
    max_answer = 1
    
    for i in range(2,min_num+1):
        #i 값으로 두수를 다 나누어 떨어진다면 최대공약수임
        if n % i == 0 and m % i == 0:
            max_answer = i
    answer.append(max_answer)
    # 최소 공배수는 각 숫자를 최대공약수로 나누고 모두 곱하기
    min_answer = (n // max_answer) * (m // max_answer) * max_answer
    
    answer.append(min_answer)
    return answer
