def solution(absolutes, signs):
    answer = []
    for num in absolutes:
        if signs[0] == True:
            answer.append(num)
            signs.pop(0)
        else:
            num = -num
            answer.append(num)
            signs.pop(0)
    return sum(answer)
