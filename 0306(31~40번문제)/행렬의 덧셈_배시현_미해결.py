def solution(arr1, arr2):
    result = []
    if len(arr1[0]) == 1:
        c = [arr1[0][0]+arr2[0][0]]
        result.append(c)
        c = [arr1[1][0]+arr2[1][0]]
        result.append(c)
        return result
    else:
        for i in range(len(arr1)):
            c = [arr1[i][0]+arr2[i][0], arr1[i][1]+arr2[i][1]]
            result.append(c)
        return result
