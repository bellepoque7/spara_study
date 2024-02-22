import math
def solution(n):
    # 어떤 숫자가 주어졌을 때 제곱근이 없다는게 대부분의 경우
    # 따라서 기본 정답을 -1 로 정하고 시작하는것.
    answer = -1
    
    n_sqrt = math.sqrt(n)
    
    # 만약 제곱근 쓴 숫자가 정수라면 정답
    if n_sqrt.is_integer():
        answer = n_sqrt
        return (answer + 1)**2
    # 또는 다음과 같이 판별
    # int(n**0.5) == n**0.5
    return answer
