def solution(n):
    answer = 0
    if n:  # 제곱근은 **을 사용해야 하는 것은 알겠는데 반대는 모르겠다. 
        answer = (n + 1) ** n
    else:
        answer = -1
    return answer
