def solution(arr):
    # 단 1개의 원소이면
    if len(arr) == 1:
        return [-1]
    
    min_value = min(arr)
    arr.remove(min_value)
    
    return arr





# def solution(arr):
    
#     # 단 1개의 원소일때 분기처리
#     if len(arr) == 1:
#         return [-1]
    
#     min_value = arr[0]
#     #메인 기능
#     for i,j in enumerate(arr):
#         if j < min_value:
#             min_value = j
#     # 배열에 대한 min_value 확인이 끝나면
#     # 그 해당하는 값을 삭제
#     arr.remove(min_value)
#     answer = arr
#     return answer
