def solution(s):
    answer = 0
    temp = ''
    if "-" not in s:
        answer = int(s)
    else:
        for i in range(1,len(s)):
            temp += s[i]
        answer = -int(temp)
    return answer
