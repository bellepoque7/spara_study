def solution(numbers):
    answer = 0
    for result in numbers:
        answer = answer + result
    answer = answer / len(numbers)

    return answer
