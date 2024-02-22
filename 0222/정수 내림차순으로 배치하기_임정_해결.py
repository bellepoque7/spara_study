def solution(n):
    # 123
    #1. 숫자 문자화: '123'
    #2. 문자를 리스트화 하기 ['1,'2','3'] 
    #3. 내림차순 정렬하고 ['3','2','1'] 
    #4. 문자화하여 숫자바꾸기 '321' -> 321
    
    answer = 0
    
    my_list = list(str(n))  #['1','2','3']
    my_list.sort(reverse = True) # ['3','2','1']
    my_str = ''.join(my_list) #'321'
      
    answer = int(my_str)
    return answer
