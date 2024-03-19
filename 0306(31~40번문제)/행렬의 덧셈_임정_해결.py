def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        #리스트 안의 리스트를 초기화 & 정의. 여기에 더한 값을 넣을 것
        my_list = []
        for j in range(len(arr1[i])):
            my_list.append((arr1[i][j] + arr2[i][j]))
        #완성된 my_list를 정답에 넣음
        answer.append(my_list)
    return answer
