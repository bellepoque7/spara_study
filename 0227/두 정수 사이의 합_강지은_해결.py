def solution(a, b):
    min_num = min(a,b)
    max_num = max(a,b)
    answer = sum(range(min_num,max_num+1))
    return answer
