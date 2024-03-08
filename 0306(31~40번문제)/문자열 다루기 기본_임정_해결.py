def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        pass
    else:
        return False
    
    for i in s:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            continue
        else:
            return False
    return True
