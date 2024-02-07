def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            answer = answer + i
    return answer

# 반복문 통해 저장할 변수 answer 초기값 0 설정하기
# for 반복문 통해서 1부터 n까지 돌기
# 각 숫자가 짝수인경우(2로 나눠질경우) 더하기
# 마지막에 return으로 출력하기
