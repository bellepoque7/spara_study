def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0: 
            answer.append(i)
            answer.sort()
        elif len(answer) == 0:
            answer.append(-1)
    return answer
  
#테스트는 통과했으나 정확도 31.3
#sort를 마지막 return에 사용하면 왜 안되는지 모르겠음
#filter 함수를 쓰는 방법이 있던데 잘 이해가 안감ㅠ
