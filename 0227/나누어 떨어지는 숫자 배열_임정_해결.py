def solution(arr, divisor):
    # 빈리스트 선언
    answer = []

    #나누어 떨어지는 연산(나머지가 없음)
    for num in arr:
        if num%divisor == 0: # 나누어 떨어지는가?
            answer.append(num) # 정답 리스트에 저장할것

    # 오름차순으로 정렬
    answer.sort()

    # element 가 하나도 없다 
    if len(answer) == 0:
        answer.append(-1)
    
    return answer
