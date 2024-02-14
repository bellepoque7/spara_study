def solution(n):
    answer = 0
    i_list = str(n).split()
    for i in i_list: 
        answer = answer + int(i)
        return answer
