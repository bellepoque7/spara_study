def solution(n):
    remain = 0
    # loop을 돈다 언제까지? 무한히 
    # 언제 끝나는가? n이 1자리 수일때(10으로 나눈 몫이 0일때)
    # 끝날때 무슨 행동을 하는가? 몫을 최종적으로 나머지합에 더한다
    while True:
        remain = remain + n % 10
        n = n // 10
        if n // 10 == 0:
            remain = remain + n % 10
            break
    return remain
