def solution(s):
    if len(s) % 2 == 1: #홀수라면
        mock = len(s) // 2 
        return s[mock]
    else: #짝수일때
        mock = len(s) // 2
        return s[mock-1:mock+1]
        
