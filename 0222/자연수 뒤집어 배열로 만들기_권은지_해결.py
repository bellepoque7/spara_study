def solution(n):
    answer=[]
    n_str=str(n)
    for i in n_str:
        answer.insert(0,int(i))
        return answer
