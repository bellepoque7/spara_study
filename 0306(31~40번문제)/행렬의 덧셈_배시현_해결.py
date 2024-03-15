# 경우의 수를 잘못 잡아서 결국 제일 늦게 풀렸다.

def solution(arr1, arr2): # ex) arr1 = [[1,2],[2,3],[3,4]]도 고려해야 한다.
    answer = [] # 최종값
    for i in range(len(arr1)): # 1차적으로 리스트 길이만큼 반복한다.
        result = [] # 초기화 필수!
        for ii in range(len(arr1[0])): # 2차적으로 리스트[0]에 대한 길이값만큼 반복한다.
            c = arr1[i][ii]+arr2[i][ii] # [4, 6, 6]이라면 다른데 다시 넣어주는 식으로..
            result.append(c)
        answer.append(result)
    return answer
