def solution(n):
    answer = []
    str_n = str(n)
    str_n_list = list(str_n)
    str_n_list.reverse()
    for i in str_n_list:
        answer.append(int(i))
    print(str_n_list)
    return answer
