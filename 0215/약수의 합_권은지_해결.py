#def solution(n):
 #   n= int(0<=3000)
  #  return sum(n)

def solution(n):
   return sum([i for i in range(1, n + 1) if n % i == 0])


def solution(n):
    n = min(max(n, 0), 3000)  # n을 0 이상 3000 이하로 제한
    divisors = [i for i in range(1, n + 1) if n % i == 0]  # n의 약수를 찾
    return sum(divisors)  # 약수의 합을 반환
