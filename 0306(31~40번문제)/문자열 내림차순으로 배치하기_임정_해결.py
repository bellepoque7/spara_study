# 대문자소문자도 순서가 있다는걸 알면됌
def solution(s):
    my_list = list(s)
    my_list.sort(reverse = True)
    return ''.join(my_list)
