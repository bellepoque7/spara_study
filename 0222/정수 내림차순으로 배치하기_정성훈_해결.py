def solution(n):
    answer = 0
    temp=''
    str_n = str(n)
    str_list = list(str_n)
    str_list.sort(reverse=True)
    
    for i in str_list:
        temp+=i
    answer = int(temp)
    return answer
