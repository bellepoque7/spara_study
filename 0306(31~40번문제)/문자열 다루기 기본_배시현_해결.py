def solution(s):
    answer = []
    if s.isdecimal():
        if len(s) == 4 or len(s) ==6:
            return True
        else:
            return False
    else:
        return False
