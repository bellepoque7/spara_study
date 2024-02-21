def solution(x, n):
    answer = []
    for i in range(n, n+1):
        answer = i.append() # append로 추가하면 될 것 같은데 하면 계속 int라서 안된다고 함. 
        return answer       # answer = str(i).append()도 해보고
                            # answer = list(i).append()도 했는데 int라서 안된다고 함. 
