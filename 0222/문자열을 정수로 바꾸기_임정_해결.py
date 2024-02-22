def solution(s):
    answer = 0
    #지표
    Flag = False
    # 조건문 
    # s가 +, 그거 떼버리기
    if s[0] == '+':
        #문자열을 두번째 문자열부터 떼어서 다시 할당
        s = s[1:]
    # s가 - 로 시작하다면 Flag 표기
    elif s[0] == '-':
        s = s[1:]
        Flag = True
    
    # 해당하는 문자열을 숫자로 바꾸기 int()
    answer = int(s)
    
    if Flag:
        return -answer
    else:
        return answer
