def solution(s):
    if len(s) % 2 == 1:
        n = divmod(len(s), 2)
        answer = list(s).pop(sum(n)-1)
        return answer
    else:
        n = int(len(s)/2)
        answer = list(s).pop(n-1) + list(s).pop(n)
        return answer
