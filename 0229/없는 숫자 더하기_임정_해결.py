def solution(numbers):
    # 결과담을 answer를 0으로 초기화
    answer = 0
    
    # 1부터 9까지의 숫자가 있는지 없는지만 확인
    # 만약에 없으면 그 숫자를 answer 누적해서 더하기
    for i in range(1,10):
        if i not in numbers:
            answer = answer + i
    return answer
