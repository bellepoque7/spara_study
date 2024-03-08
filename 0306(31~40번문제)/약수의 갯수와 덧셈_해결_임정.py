#약수를 구하는 함수를 따로 뺴는게 포인트
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if check_num(i) % 2 == 0:
            answer += i
        else:
            answer -= i 
    return answer

def check_num(n):
    num_list = []
    for i in range(1,n+1):
        if n % i == 0:
            num_list.append(i)
    return len(num_list)
            
