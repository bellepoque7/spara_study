def solution(n):
    #my_list = []
    answer = n - 1
    for i in range(1, n):
        if n % i == 1:
            # 방법1: 나머지가 1이 되게하는 모든 값을 리스트에 저장하는 방법
            #my_list.append(i)
            # 방법2: 
            answer = min(answer, i)
    return answer
